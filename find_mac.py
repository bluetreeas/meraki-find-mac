from time import sleep
import meraki
import argparse


class MerakiApi:
    def __init__(self, meraki_api_key, meraki_org_id):
        self.meraki_org_id = meraki_org_id
        self.dashboard = meraki.DashboardAPI(
            meraki_api_key,
            print_console=False,
            suppress_logging=True
        )

    def _get_org_name(self, meraki_org_id):
        my_organizations = self.dashboard.organizations.getOrganizations()
        org_name = "default"

        for org in my_organizations:
            if org['id'] == meraki_org_id:
                org_name = org['name']
        return org_name

    def _get_networks(self):
        try:
            networks = self.dashboard.organizations.getOrganizationNetworks(self.meraki_org_id)
            return networks
        except meraki.exceptions.APIError:
            return None

    def _get_network_clients(self, network_id):
        try:
            clients = self.dashboard.networks.getNetworkClients(network_id, perPage=1000)
            return clients
        except meraki.exceptions.APIError:
            return None

    def get_device_client_data(self, serial, mac):
        mac = mac.lower().replace(':', '').replace('-', '')

        try:
            clients = self.dashboard.devices.getDeviceClients(serial)
            for client in clients:
                if client['mac'].lower().replace(':', '') == mac:
                    return client
            return None
        except meraki.exceptions.APIError:
            return None

    def find_mac_by_network(self, mac):
        mac = mac.lower().replace(':', '').replace('-', '')
        networks = self._get_networks()

        if networks:
            for network in networks:
                print(f'Checking network: {network["name"]}')
                network_clients = self._get_network_clients(network['id'])

                if network_clients:
                    for client in network_clients:
                        if client['mac'].lower().replace(':', '') == mac:
                            return client

                print("    MAC not found in this network")
        else:
            print("Error: Please verify meraki api key and org id")
            return None

    def blink_device_leds(self, serial):
        response = self.dashboard.devices.blinkDeviceLeds(serial)
        return response


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
        meraki_api.blink_device_leds(client.get('recentDeviceSerial'))
        sleep(20)
        print(f'    Blinking device leds of {client.get("recentDeviceName")} completed.')


if __name__ == "__main__":
    main()
