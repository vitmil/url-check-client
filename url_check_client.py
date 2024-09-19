#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Vittorio Milazzo - <vittorio.milazzo@gmail.com>

# url_check
url_check_client is a client to make requests vs RESTful Web Services running on https://url-check.duckdns.org.

For more info about the service, go to: https://url-check.duckdns.org/about

Note:
If your firewall blocks outgoing connection, to reach the service on https://url-check.duckdns.org, 
outgoing traffic must be allowed for:

 - tcp port 8000 for http requests
 - tcp port 8443 for https requests

 # Syntax to pass target: 

 - output formatted text
   url_check_client.py  -t www.site.com
   url_check_client.py  -t http://site.com
   url_check_client.py  -t https://site.com
    
 - output json format wants -o json argument
   url_check_client.py -t www.site.com  -o json


# syntax to pass file: 

- output formatted text
  url_check_client.py -f <file> 
  url_check_client.py -f <file> -o hr 

- output json format wants -o json argument
  url_check_client.py -f <file> -o json 

        
== TODO ==
- passare ulteriore api-key (unlimited). In questo caso sostituisce l' api-key hardcodata
"""

# == Modules ==
#
import os
import sys
import argparse 
import requests
#import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


# == Glob Vars ==
#
# define the url_check_server to point
#server = "url-check.vimi.space" # host prod
url_check_server = "129.152.26.254"        # host prod
#url_check_server = "192.168.56.100"       # host dev

# Public api-key (limited)
API_KEY = "f438988e-4acc-4fb3-ae81-0a0c3729395a"

# Argparse 
parser = argparse.ArgumentParser(
    description = "Url Check Client - command-line client to make requests vs URL CHECK", 
    #epilog = "Syntax example to scan single target: url_check_client -t www.google.com \n Syntax example to scan multiple targets passing a file: url_check_client -u <username> -p <password> -f <file_with_urls>"
    )
## argparse combinational options 
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-t', dest='target',   type=str, help="site URL to scan")
group.add_argument('-f', dest='url_file_to_upload', type=str, help="File with list of site URL to scan")
#
## Mondatory arguments
#parser.add_argument('--username', '-u', dest='username', type=str, help='username to authenticate', required=True) 
#parser.add_argument('--password', '-p', dest='password', type=str, help='password', required=True) 
#
## optional params because: default='hr'
parser.add_argument('--output', '-o', dest='output', type=str, help='output format: hr or json', default='hr')
parser.add_argument('--conntype', '-c', dest="conn_type", type=str, default='http', help="to make the request using https port (8443)")
#
# create obj args
args = parser.parse_args()
#
# assign argparse variables values to the follow vars (maintaining the same same on destination vars)
target = args.target
url_file_to_upload = args.url_file_to_upload
#username = args.username
#password = args.password
target = args.target
output = args.output
conn_type = args.conn_type
# /END argparse


# == Routine ==
#
def print_message():
    print("For further info about service, visit https://129.152.26.254")
    print("To report a bug send an email to vimi.code@gmail.com.\n")


def start():
    # if target is passed (-t)
    if target:
        if conn_type == "https":
            url = f"https://{url_check_server}:8443/scanurl/?target={target}&output={output}" # https request
        else:
            url = f"http://{url_check_server}:8000/scanurl/?target={target}&output={output}" # http  request

        # Set the headers
        headers = {"apikey": API_KEY}
        # Send the GET request
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code != 200:
            responses = [response.json()['message'], "Reason: " + response.reason, "Status Code: " + str(response.status_code)]
            for response in responses:
                print(response)
            print()
        else: 
            print(response.text)          


    # if file is passed(-f or --file)
    if url_file_to_upload:

        if not os.path.isfile(url_file_to_upload):
            print(f'\n[ERROR]: file {url_file_to_upload} not found\n')
            sys.exit(1)
    
        if conn_type == "https":
            url = f"https://{url_check_server}:8443/scanfile/?output={output}"
        else:
            url = f"http://{url_check_server}:8000/scanfile/?output={output}"

        # Set the headers
        headers = {
            "accept": "text/plain",
            # se abilitato non restituisce i risultati, ma {"detail":"Missing boundary in multipart."}
            #"Content-Type": "multipart/form-data"
            "apikey": API_KEY
        }

        # Set the file data
        files = {
            #"file": ("file_name.txt", open(url_file_to_upload, "rb")) 
            "file": ("file_name.txt", open(url_file_to_upload, "rb"), "text/plain") 
        }

        # Send the POST request
        response = requests.post(url, headers=headers, files=files, verify=False)

        if response.status_code != 200:
            responses = [response.text.strip('\n'), "Reason: " + response.reason, "Status Code: " + str(response.status_code)]
            for response in responses:
                print(response)
            print()          
        else: 
            print(response.text)            

# start script
#print()
start()
print_message()
