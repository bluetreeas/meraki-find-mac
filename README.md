# Meraki - Find MAC

This script takes a MAC address as input, and returns where it's connected and blink the LED of the device.


## Requirements

- Python 3.6+
- Administrator access to Meraki Dashboard

## Getting started

1. Install needed python packages

```
pip3 install -r requirements.txt
```

2. Set environment variables

```
export MERAKI_API_KEY = <YOUR MERAKI API KEY>
```

3. Run script

```
python3 find_mac.py
```

4. Input MAC address and org id

```
```