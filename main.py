#!/usr/bin/env python3
import sys
import asyncio
from MariaDB import MariaDB
from Scanner import Scanner

async def main(argv):
    try:
        db = MariaDB()
    except:
        print("Database error occurred")
        db = None

    try:
        interval = int(argv[0])
    except:
        interval = 60

    scanner = Scanner(db)
    await scanner.startScanning(interval)

if __name__ == "__main__":
    try:
        asyncio.run(main(sys.argv[1:]))
    except KeyboardInterrupt:
        print("\nStopping...")
