import asyncio
from functools import partial
from bleak import BleakScanner
from datetime import datetime
from Database import Database

class Scanner:
    __device_mac = "EC:0E:A4:EB:60:3A"
    __db: Database = None

    def __init__(self):
        pass

    def __hexToInt(self, hexValue):
        return int(hexValue, base=16)

    def __detection_callback(self, device, advertisement_data):
        if 1177 in advertisement_data.manufacturer_data:
            now = datetime.now()
            mac = device.address
            data = advertisement_data.manufacturer_data[1177].hex()
            temp = round(self.__hexToInt(data[2:6]) * 0.005, 2)
            humidity = round(self.__hexToInt(data[6:10]) * 0.0025, 2)
            atmosphericPressure = round((self.__hexToInt(data[10:14]) + 50000) / 100, 2)

            if self.__db:
                row = self.__db.insert_measurement((now, device.address, temp, humidity, atmosphericPressure))
                print("row", row)

            print("time", now.strftime("%H:%M:%S"))
            print("mac", mac)
            print("temp", temp)
            print("humidity", humidity)
            print("atmosphericPressure", atmosphericPressure)
            print("")

    async def startScanning(self, db: Database, sleep = 5.0):
        self.__db = db
        while True:
            async with BleakScanner() as scanner:
                scanner.register_detection_callback(self.__detection_callback)
                await asyncio.sleep(sleep)