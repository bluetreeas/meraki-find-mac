# Meraki - Find MAC

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/bluetreeas/meraki-find-mac)

This script takes a MAC address as input, and returns where it's connected and blink the LED of the device.

## Requirements

- Python 3.6+
- Administrator access to Meraki Dashboard

## Instructions

1. Enable API access in your Meraki organization: Meraki Dashboard -> Organization -> Settings -> Dashboard API access

2. Generate your API key: Meraki Dashboard -> My profile -> API access

3. Get Meraki Org ID (You must be logged in to Meraki Dashboard first): https://api.meraki.com/api/v1/organizations

4. Install needed python packages

```
pip install -r requirements.txt
```

5. Run script with the required arguments (MAC address format is not case sensitive, and support notation with both ":", "-" and nothing between octets)

```
python find_mac.py <MERAKI_KEY> <MERAKI_ORG_ID> <MAC_ADDRESS>
```

6. Run around and see if you find the blinking LEDs :)

## Example 

![Alt text](./find_mac_example.png?raw=true "Find MAC example")
