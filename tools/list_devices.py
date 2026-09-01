import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover(return_adv=True)

    for address, (device, adv) in devices.items():
        print("\n------------------------")
        print("Device:", device)

        print("local_name:", adv.local_name)
        print("manufacturer_data:", adv.manufacturer_data)
        print("service_data:", adv.service_data)
        print("service_uuids:", adv.service_uuids)
        print("tx_power:", adv.tx_power)
        print("rssi:", adv.rssi)
        print("platform_data:", adv.platform_data)

asyncio.run(main())