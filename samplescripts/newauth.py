#!/usr/bin/env python3
import yaml

from authlib.client import OAuth2Session

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

refresh_uri = "oauth2/token"

session = OAuth2Session(client_id, client_secret)
token = session.fetch_access_token(config["url"] + "/oauth2/authorize/central/api/login")

# data =

print(token)

# https://central-pvt-apigw.arubathena.com/oauth2/token