## HPE Aruba Central Python REST Client


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
