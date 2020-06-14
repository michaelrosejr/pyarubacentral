## Aruba Central Python RESTful module


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

A Python module for use with Aruba Central. The aim is to make life easier for people who are not primarily programmers, but need to interact with services in a programmatic manner (e.g. automation).

This python module is used primarily to refresh expired access tokens and generate new refresh tokens as well. It also supports profiles, so you can setup multiple Aruba Central accounts and easily include those tokens in your script and easily switching between accounts by passing the profile variable. 

The example script is included to show a list of users in Aruba Central or display when an access token will expire.

### Contents
  * [Features](#features)
  * [Installation](#installation)
  * [Prerequisites](#prerequisites)
  * [Usage](#usage)
  * [Python Module](#python-module)
  * [License](#license)
  * [Contribute](#contribute)
  * [Disclaimer](#disclaimer)

### Features

 - CLI script to refresh access tokens 
 - CLI script to generate a new refresh and access token 
 - Python module to import to generate and refresh tokens automatically as the script it executed.
 ![enter image description here](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/refresh.png)
 ![enter image description here](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/newtoken.png)

### Installation
To install directly into your python environment please install with the following command:

    pip install pyarubacentral

If you prefer to clone this GitHub project, please be sure to run  

    
    git clone git@github.com:michaelrosejr/pyarubacentral.git
    pipenv shell

before you start coding.



### Prerequisites

The following Python module assumes you have already created an API account on Aruba Central, requested a code and exchanged that code for a token. For details on how to do setup an account for API access in Aruba Central, please go to the [help documentation]([https://help.central.arubanetworks.com/latest/documentation/online_help/content/api/api_bootstrap-sdwan.htm?Highlight=APi](https://help.central.arubanetworks.com/latest/documentation/online_help/content/api/api_bootstrap-sdwan.htm?Highlight=APi)) in Aruba Central.

### Usage

`
arubacentral --configure
`

Once configured, open your editor and edit the following files 
`
~/.arubacentral/accounts.yml
~/.arubacentral/config.yml
~/.arubacentral/regions.yml
`

![accounts.yml](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/accounts.yml.example.png)

![config.yaml](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/config.yaml.example.png)


All tokens are stored in `~/.arubacentral/tokens/profilename.tokens.json`
should you need to edit them.

To refresh an expired token:
`arubacentral --refresh [profile_name]`

![enter image description here](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/refresh.png)

To generate a new access and refresh token:
`arubacentral --newtoken [profile_name]`

![enter image description here](https://raw.githubusercontent.com/michaelrosejr/pyarubacentral/media/newtoken.png)

### Python Module
To use it as a python module within your code. See the [example](https://github.com/michaelrosejr/pyarubacentral/blob/master/samplescripts/exampleauth.py)

```
import pyarubacentral
profile = "ACME"

# Return User List from Aruba Central
session = pyarubacentral.start_session(profile)
access_token = pyarubacentral.check_if_expired(profile, session)
print(session.get_user_account_list(access_token))
```



### License
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

### Contribute
If you're interested in contributing to add feature or fix bugs, please open an issue to discuss and Pull Requests to fix an identified bug. PR's are always welcome! Please be sure to have a detailed PR description that clearly describes the problem and solution.


### Disclaimer

This module is incomplete. It does not have all the API calls available via Aruba Central. If you see something you need from the swagger client, let us know and we'll do our best to add it to this module. Even better, add it yourself and we'll help you merge your code in this repository.

This is not an 'official' SDK and is not guaranteed to always work with Aruba Central's APIs, on all platforms, or without eating up all your machine's resources. But we'll do our best to keep it in good shape, are happy to take suggestions for improvements, and are open to collaborations. License info is [here](LICENSE.md).