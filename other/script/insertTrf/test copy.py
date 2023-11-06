import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## replace ????

curl = """
curl 'https://cnshaapppwv314.asia.pwcinternal.com/trf/api/oss/Insert' \
  -H 'authority: cnshaapppwv314.asia.pwcinternal.com' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer eyJhb????VD4dBZbJ4U' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'dnt: 1' \
  -H 'origin: https://apphkdm470.digitalmaker.asia.pwcinternal.com' \
  -H 'pragma: no-cache' \
  -H 'referer: https://apphkdm470.digitalmaker.asia.pwcinternal.com/' \
  --data-raw \
"""

import csv
import os
import time
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def getpayLoad(name,version,link):
    payload = {
        "docID":"3224???????6dc",
        "name":name,
        "version":version,
        "license":["1"],
        "linkTo":link,
        "itemID":"",
        "isModified":0,
        "isDiff":0
        }
    return payload

with open('Book4.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(len(row),row)
        payload = getpayLoad(row[0],row[1],row[2])
        print(payload)
        #r = requests.post(url, data=json.dumps(payload), headers=headers,verify=False)
        print(curl + "'" +json.dumps(payload)+"'")
        status, output = subprocess.getstatusoutput(curl + "'" +json.dumps(payload)+"'")
        print(status,output)
        time.sleep(3)


