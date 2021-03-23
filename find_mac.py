from utils.meraki_api import MerakiApi
from time import sleep
import os

MERAKI_API_KEY = os.getenv('MERAKI_API_KEY')
MERAKI_ORG_ID = "SET MERAKI ORG ID HERE"
MAC_ADDRESS = "SET MAC ADDRESS HERE"


def main():
    meraki_api = MerakiApi(
        meraki_api_key=MERAKI_API_KEY,
        meraki_org_id=MERAKI_ORG_ID,
    )

    client = meraki_api.find_mac_by_network(MAC_ADDRESS)

    if client:
        device_client = meraki_api.get_device_client_data(client["recentDeviceSerial"], MAC_ADDRESS)
        print(f'    MAC found: {client["description"]} ({client["mac"]})')
        print(f'    Last connected to: {client["recentDeviceName"]} ({client["recentDeviceSerial"]})')
        print(f'    Connection details: Port: {device_client["switchport"]}, VLAN: {device_client["vlan"]}, IP: {device_client["ip"]}')

        print(f'    Start blinking device leds on {client["recentDeviceName"]} for 20 seconds...')
        meraki_api.blink_device_leds(client['recentDeviceSerial'])
        sleep(20)
        print(f'    Blinking device leds of {client["recentDeviceName"]} completed.')


if __name__ == "__main__":
    main()
