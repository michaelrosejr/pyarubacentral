#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.
"""
import requests
import json
import time, datetime
import yaml

from unittest import TestCase
from nose.plugins.skip import SkipTest

from pyarubacentral.auth import *
from pyarubacentral.monitoring import *
from pyarubacentral.configuration import *
from pyarubacentral.usermgmt import *

__author__ = "Michael Rose Jr."
__maintainer__ = "Michael Rose Jr."
__email__ = "michael@michaelrosejr.com"
__status__ = "Production"

def read_config():
    with open("config.yml", 'r') as ymlfile:
        data = yaml.load(ymlfile)
    return data


# Read config file
config = read_config()
client_id = config["client_id"]
client_secret = config["client_secret"]
tokenfile = config["tokenfile"]
if config["envapi"] == "prod":
    baseurl = "https://app1-apigw.central.arubanetworks.com"
else:
    baseurl = "https://internal-apigw.central.arubanetworks.com"

with open(tokenfile) as exjsonfile:
    sessiondata = json.load(exjsonfile)

current_time = time.time() * 1000

refresh_token = sessiondata["refresh_token"]
# sessiondata = sessiondata["sessiondata"]
created_at = sessiondata["created_at"]
expires_in = sessiondata["expires_in"]
expires_at = ((created_at / 1000) + expires_in) * 1000
sessiondata["baseurl"] = baseurl


if current_time  > expires_at:
    print("Refreshing token")
    url = baseurl + "/oauth2/token"
    payload = {'refresh_token': refresh_token, 'client_id': client_id, 'client_secret': client_secret,
               'grant_type': 'refresh_token'}
    response = requests.post(url, params=payload)
    tokenconfig = response.json()
    tokenconfig['created_at'] = current_time
    with open(tokenfile, "w") as exjsonfile:
        json.dump(tokenconfig, exjsonfile)


class TestGetMACTable(TestCase):
    """
    Test Case for pyarubaaoss vlans get vlans function
    """
    def SetUp(self):
        pass
    def TearDown(self):
        pass
    def get_users():
        v2_users = Usermgmt(sessiondata, 'none')
        print(dir(v2_users.get_accounts_v2_users()))

print(TestGetMACTable.get_users())
