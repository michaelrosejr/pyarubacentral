#!/usr/bin/env python3
import time
from flask import Flask
from flask import render_template
import requests
import json
import click
import time, datetime
import yaml
import logging

from pyarubacentral import auth
import pyarubacentral.get_switches as switches
import pyarubacentral.get_groups as groups
import pyarubacentral.get_networks as networks
import pyarubacentral.get_template_vars as template_vars
import pyarubacentral.get_devices as get_devices
import pyarubacentral.wireless as wireless
from pyarubacentral import monitoring
from pyarubacentral import configuration

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
username = config["username"]
password = config["password"]
tokenfile = config["tokenfile"]
if config["envapi"] == "prod":
    baseurl = "https://app1-apigw.central.arubanetworks.com"
else:
    baseurl = "https://internal-apigw.central.arubanetworks.com"

with open(tokenfile) as exjsonfile:
    sessiondata = json.load(exjsonfile)

current_time = time.time() * 1000
# print(sessiondata)
# if(sessiondata['error_description'] == 'Invalid client authentication')
#     auth.get_auth_code('')

check_refresh_token = sessiondata.get('refresh_token')
if check_refresh_token is not None:
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
else:
    cookies = dict(auth.CentralAuth.get_login_cookies(config))
    auth_code = json.loads(auth.CentralAuth.get_auth_code(cookies, config))
    tokens = auth.CentralAuth.get_access_tokens(config, auth_code['auth_code'])
    tokenconfig = tokens.json()
    tokenconfig['created_at'] = current_time
    # print(tokenconfig)
    with open(tokenfile, "w") as exjsonfile:
        json.dump(tokenconfig, exjsonfile)

app = Flask(__name__)



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/aplist')
def aplist():
    aplist = wireless.get_wifi_aps(sessiondata, 'USOC')
    print(aplist)
    return render_template('aplist.html', title='Home', aplist=aplist['aps'])

@app.route('/clients')
def cients():
    clientlist = wireless.get_wifi_clients(sessiondata, 'USOC')
    print(clientlist)
    return render_template('clients.html', title='Home', clientlist=clientlist['clients'])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
