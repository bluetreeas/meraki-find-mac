# Meraki - Find MAC

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/bluetreeas/meraki-find-mac)

This script takes a MAC address as input, and returns where it's connected and blink the LED of the device.


## Requirements

- Python 3.6+
- Administrator access to Meraki Dashboard

## Instructions

1. Install needed python packages

```
pip install -r requirements.txt
```

2. Run script with the required arguments

```
python find_mac.py MERAKI_KEY MERAKI_ORG_ID MAC_ADDRESS
```

3. Run around and see if you find the blinking LEDs :)
