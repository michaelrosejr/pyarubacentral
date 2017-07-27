#!/bin/bash

CLIENTID=aa5eb84c499e4964beb41766ff4975e2
CODE=dd2ae8e9bdab4f2488630bbe57455412
CLIENTSECRET=b6bf3aa2d482455ba3e289b6f1d5ad6f
{"auth_code":"3fd82589e84e43c78d737c2a09c3e86a"}

#curl -X POST 'https://app1-apigw.central.arubanetworks.com/oauth2/token?client_id=aa5eb84c499e4964beb41766ff4975e2&grant_type=authorization_code&client_secret=b6bf3aa2d482455ba3e289b6f1d5ad6f'
curl -H "Content-Type: application/json" -X GET 'https://app1-apigw.central.arubanetworks.com/oauth2/authorize/central?client_id=aa5eb84c499e4964beb41766ff4975e2&response_type=code&scope=all'
