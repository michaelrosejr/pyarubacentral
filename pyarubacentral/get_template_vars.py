#!/usr/bin/env python3

import requests, json
from pyarubacentral import auth


def get_template_vars(access_token, serialnumber):
    url = "https://app1-apigw.central.arubanetworks.com/configuration/v1/devices/" + serialnumber + "/template_variables"
    payload = {'access_token': access_token}
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=payload, headers=headers)

    return response.json()