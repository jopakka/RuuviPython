#!/usr/bin/env python3
import asyncio
from MariaDB import MariaDB
from Scanner import Scanner

async def main():
    try:
        db = MariaDB()
    except:
        print("Database error occurred")
        db = None

    scanner = Scanner(db)
    await scanner.startScanning()

if __name__ == "__main__":
    asyncio.run(main())
