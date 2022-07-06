#!/usr/bin/env python3
import os
import mariadb
import atexit
from dotenv import load_dotenv

class MariaDBError(Exception):
    pass

class MariaDB():
    __tables = [
        """CREATE TABLE IF NOT EXISTS measurements(
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            mac VARCHAR(17) NOT NULL,
            timestamp TIMESTAMP NOT NULL,
            temperature FLOAT NOT NULL,
            humidity FLOAT NOT NULL,
            pressure FLOAT NOT NULL
        );"""
    ]
    __conn = None
    __cursor = None

    def __init__(self):
        load_dotenv()
        conn = self.__createConnection()
        self.__conn = conn
        self.__cursor = conn.cursor()
        self.__createTables()
        atexit.register(self.__closeConnection)

    def __createConnection(self):
        try:
            conn = mariadb.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=int(os.getenv("DB_PORT")),
                database=os.getenv("DB_NAME")
            )
            print(f"MariaDB version: {mariadb.mariadbapi_version}")
            return conn
        except mariadb.Error as e:
            print(f"MariaDB error: {e}")
        except Exception as e:
            print(f"MariaDB general error: {e}")

    def __closeConnection(self):
        if self.__conn != None:
            print("Closing db connection")
            self.__conn.close()

    def __createTables(self):
        for table in self.__tables:
            self.__cursor.execute(table)

    def insertMeasurement(self, measurement):
        sql = """INSERT INTO measurements(timestamp, mac, temperature, humidity, pressure)
            VALUES(?, ?, ?, ?, ?)"""
        self.__cursor.execute(sql, measurement)
        self.__conn.commit()
        return self.__cursor.lastrowid
