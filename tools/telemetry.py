import asyncio
from bleak import BleakScanner, BleakClient

async def main():
    devices = await BleakScanner.discover()

    for d in devices:
        print(d.name, d.address)

    address = "XX:XX:XX:XX:XX:XX"

    async with BleakClient(address) as client:
        for service in client.services:
            print("SERVICE:", service.uuid)

            for char in service.characteristics:
                print(
                    "  CHAR:",
                    char.uuid,
                    char.properties
                )

asyncio.run(main())