#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth

def get_device_inventory(sessiondata, type):
    url = "https://app1-apigw.central.arubanetworks.com/device_inventory/v2/devices?sku_type=" + type
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()
