import asyncio
from bleak import BleakScanner
from datetime import datetime

# https://github.com/ruuvi/ruuvi-sensor-protocols/blob/master/dataformat_05.md

device_mac = "EC:0E:A4:EB:60:3A"
sleep = 5.0

def hexToInt(hexValue):
    return int(hexValue, base=16)

def detection_callback(device, advertisement_data):
    if device.address == device_mac:
        # print(device.address, "RSSI:", device.rssi, advertisement_data)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        data = advertisement_data.manufacturer_data[1177].hex()
        temp = round(hexToInt(data[2:6]) * 0.005, 2)
        humidity = round(hexToInt(data[6:10]) * 0.0025, 2)
        atmosphericPressure = round((hexToInt(data[10:14]) + 50000) / 100, 2)
        print("Current time", current_time)
        print("temp", temp)
        print("humidity", humidity)
        print("atmosphericPressure", atmosphericPressure)
        print("")

async def main():
    while True:
        async with BleakScanner() as scanner:
            scanner.register_detection_callback(detection_callback)
            await asyncio.sleep(sleep)

if __name__ == "__main__":
    asyncio.run(main())

