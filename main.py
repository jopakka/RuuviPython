#!/usr/bin/env python3
import asyncio
from Database import Database
from Scanner import Scanner

async def main():
    db = Database()
    scanner = Scanner()
    await scanner.startScanning(db)

if __name__ == "__main__":
    asyncio.run(main())
