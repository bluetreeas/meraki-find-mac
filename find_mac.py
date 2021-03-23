from utils.meraki_api import MerakiApi
from time import sleep
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='MERAKI_KEY', help="Meraki API key")
    parser.add_argument(dest='MERAKI_ORG_ID', help="Meraki ORG id")
    parser.add_argument(dest='MAC_ADDRESS', help="MAC address to search for")
    args = parser.parse_args()

    meraki_api = MerakiApi(
        meraki_api_key=args.MERAKI_KEY,
        meraki_org_id=args.MERAKI_ORG_ID,
    )

    client = meraki_api.find_mac_by_network(args.MAC_ADDRESS)

    if client:
        device_client = meraki_api.get_device_client_data(client.get("recentDeviceSerial"), args.MAC_ADDRESS)
        print(f'    MAC found: {client.get("description")} ({client.get("mac")})')
        print(f'    Last connected to: {client.get("recentDeviceName")} ({client.get("recentDeviceSerial")})')
        print(f'    Connection details: Port: {device_client.get("switchport")}, VLAN: {device_client.get("vlan")}, IP: {device_client.get("ip")}')

        print(f'    Start blinking device leds on {client.get("recentDeviceName")} for 20 seconds...')
        #meraki_api.blink_device_leds(client.get('recentDeviceSerial'))
        #sleep(20)
        print(f'    Blinking device leds of {client.get("recentDeviceName")} completed.')


if __name__ == "__main__":
    main()
