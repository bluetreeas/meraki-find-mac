import meraki


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
