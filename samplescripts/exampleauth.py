import pyarubacentral

# print(pyarubacentral.Config())

#
# Set which profile to use from ~/.arubacentral/config.yaml
#
profile = "ACME"


#
# Return User List from Aruba Central
#
# Start the session
session = pyarubacentral.start_session(profile)
# Check if the current acess tokens are expired, 
# if expired, refresh the token and continue
# if not, continue
access_token = pyarubacentral.check_if_expired(profile, session)

# Use access tokens and get the list of users
print(session.get_user_account_list(access_token))


#
## Check when a access token expires
# session = pyarubacentral.start_session(profile)
# access_token = pyarubacentral.check_if_expired(profile, session)
# print(pyarubacentral.expires(profile))