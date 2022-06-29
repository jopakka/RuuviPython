import os
import sqlite3
from sqlite3 import Error

class Database:
    __tables = [
        """CREATE TABLE IF NOT EXISTS measurements(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mac TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            temperature NUMERIC NOT NULL,
            humidity NUMERIC NOT NULL,
            pressure NUMERIC NOT NULL
        );"""
    ]

    __conn = None

    def __init__(self):
        self.create_connection()
        for t in self.__tables:
            self.create_table(t)

    def create_connection(self):
        try:
            self.__conn = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/sqlite.db")
            print(f"Sqlite version: {sqlite3.version}")
        except Error as e:
            print(e)

    def close(self):
        if self.__conn:
            self.__conn.close()

    def create_table(self, table_string):
        if self.__conn:
            try:
                cur = self.__conn.cursor()
                cur.execute(table_string)
                self.__conn.commit()
            except Error as e:
                print(e)

    def insert_measurement(self, measurement):
        sql = """INSERT INTO measurements(timestamp, mac, temperature, humidity, pressure)
              VALUES(?, ?, ?, ?, ?)"""
        cur = self.__conn.cursor()
        cur.execute(sql, measurement)
        self.__conn.commit()
        return cur.lastrowid