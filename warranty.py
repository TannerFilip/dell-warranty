#!/bin/python3

'''
USAGE:
$ python warranty.py list.txt

1. Set "apikey" to the API key obtained from Dell TechDirect.
2. Create file with serial numbers, one per line, no line endings

'''

import time
import requests
import fileinput
import sys


fileName = sys.argv[1]


api_url = 'https://sandbox.api.dell.com/support/assetinfo/v4/getassetwarranty'
headers = {"Content-Type":"application/x-www-form-urlencoded",
           "apikey":"aaaaaaaaaaaaaaaaaaaaaaaaaa",
           "accept":"application/json"}



with open(fileName, 'r') as serialNumber:
        for line in serialNumber:
                payload = {"ID":""}
                payload['ID'] = line
                # Actually make the request
                try:
                    r = requests.post(api_url, headers=headers, data=payload).json()

                    print('Serial:', payload['ID'], 'Expires', r['AssetWarrantyResponse'][0]['AssetEntitlementData'][0]['EndDate'])
                except:
                    print('Invalid ID:', payload['ID'])
                    pass
                # Too lazy to make it actually output a csv, this is good enough

                time.sleep(1) # Wait a sec before doing it again, so to not hit the API too quickly
