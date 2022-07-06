import asyncio
import time
from bleak import BleakScanner
from datetime import datetime

class Scanner:
    __db = None

    def __init__(self, db):
        self.__db = db
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
                row = self.__db.insertMeasurement((now, mac, temp, humidity, atmosphericPressure))
                # print("row", row)

            # print("time", now.strftime("%H:%M:%S"))
            # print("mac", mac)
            # print("temp", temp)
            # print("humidity", humidity)
            # print("atmosphericPressure", atmosphericPressure)
            # print("")

    async def startScanning(self, interval = 15):
        print("Starts scanning")
        scanner = BleakScanner()
        scanner.register_detection_callback(self.__detection_callback)
        scanTime = 5
        waitTime = interval - scanTime if interval - scanTime > 0 else 0
        print(f"Scan interval: {waitTime + scanTime}s")
        while True:
            await scanner.start()
            await asyncio.sleep(scanTime)
            await scanner.stop()
            await asyncio.sleep(waitTime)