import pyarubacentral

# print(pyarubacentral.Config())

profile = "ACME"

## Check when a access token expires
# session = pyarubacentral.start_session(profile)
# access_token = pyarubacentral.check_if_expired(profile, session)
# print(pyarubacentral.expires(profile))

# Return User List from Aruba Central
session = pyarubacentral.start_session(profile)
access_token = pyarubacentral.check_if_expired(profile, session)
print(session.get_user_account_list(access_token))