## Aruba Central Python REST Client 
### pyarubacentral


A Python module for use with Aruba Central. Its aim is to make life easier for people who are not primarily programmers, but need to interact with services in a programmatic manner (e.g. automation)

To install directly into your python environment please use the **pip install pyarubacentral** command

### Prequisites

The following Python module assumes you have already created an API account on Aruba Central, requested a code and exchanged that code for a token. For details on how to do these steps, please follow the steps in [this guide](http://help.central.arubanetworks.com/2.2.6/documentation/online_help/content/pdfs/aruba%20central%20api%20reference%20guide.pdf)

To use the ```sampleapp.py``` script include, please do the following.
### Download a Token
To obtain tokens using the offline token method, complete the following steps:

1. Click **Maintenance >API Gateway**. The **API Gateway** page is displayed.
2. Click **Authorized Apps & Tokens**.
3. Click **View Tokens**. The **Token List pop-up** window opens.
4. To download tokens, click **Download Token**.

Once you have downloaded your first token, copy and paste that token into the file ```token.json``` file. Once you have the token in this file, the ```sampleapp.py``` script with refresh the token when it expires.

A ```sampleapp.py``` script has been included to understand how the module works.

### Disclaimer

This module is incomplete. It does not have all the API calls available via Aruba Central. If you see something you need from the swagger client, let us know and we'll do our best to add it to this module. Even better, add it yourself and we'll help you merge your code in this repository.

This is not an 'official' SDK and is not guaranteed to always work with Aruba Central's APIs, on all platforms, or without eating up all your machine's resources. But we'll do our best to keep it in good shape, are happy to take suggestions for improvements, and are open to collaborations. License info is [here](LICENSE.md).