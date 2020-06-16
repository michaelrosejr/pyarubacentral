import pyarubacentral

## To see detailed logging
# import logging
# logging.basicConfig(level=logging.DEBUG)

## See Config settings
# print(pyarubacentral.Config())

#
## Set which profile to use from ~/.arubacentral/config.yaml
#
profile = "ACME"

## Start the session
session = pyarubacentral.start_session(profile)
## Check if the current acess tokens are expired, 
## if expired, refresh the token and continue
## if not, continue
access_token = pyarubacentral.check_if_expired(profile, session)

#
## Return User List from Aruba Central
#
## Use access tokens and get the list of users
print(session.get_user_account_list(access_token))

#
## Return when access token will expire
#
## Use access tokens and get the list of users
# print("Expires: {}".format(pyarubacentral.expires(profile)))