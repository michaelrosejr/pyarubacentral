#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth

def get_central(sessiondata, url):
    """
    Login and get Aruba Central data
    """
    payload = {'access_token': sessiondata['access_token']}
    headers = {"Accept": "application/json"}

    try:
        r = requests.get(url, params=payload, headers=headers)
        if r.status_code != 200:
            print('Status:', r.status_code, 'Headers:', r.headers,
                  'Error Response:', r.reason)
        return r.text
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + sys._getframe().f_code.co_name + ": An Error has occured"


class DeviceInventory():
    """ Central Device Inventory APIs """
    def __init__(self, sessiondata, pvalue):
        self.sessiondata = sessiondata


    def get_devices(self, type):
        """
        List devices
            Returns all devices based on type
        """

        url = self['baseurl'] + "/device_inventory/v2/devices?sku_type=" + type

        response = get_central(self, url)

        return response