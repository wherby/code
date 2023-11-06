import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## not working for post

url = 'https://cnshaapppwv314.asia.pwcinternal.com/trf/api/edithistory/Insert'
payload = {
"docID":"3224?????6dc",
"name":"zustand",
"version":"4.4.1",
"license":[],
"linkTo":"https://www.npmjs.com/package/zustand",
"itemID":"",
"isModified":0,
"isDiff":0
}

def getpayLoad(name,version,link):
    payload = {
        "docID":"3224????be96dc",
        "name":name,
        "version":version,
        "license":[],
        "linkTo":link,
        "itemID":"",
        "isModified":0,
        "isDiff":0
        }
    return payload
# Adding empty header as parameters are being sent in payload
headers = {
       "authority": "cnshaapppwv314.asia.pwcinternal.com",
    "accept": "application/json, text/plain, */*",
    "authorization": "Bearer eyJh???bJ4U",
    "content-type": "application/json;charset=UTF-8",
    "dnt": "1",
  ##  "path":"/trf/api/oss/Insert",
    "origin": "https://apphkdm470.digitalmaker.asia.pwcinternal.com",
    "pragma": "no-cache",
        "cache-control": "no-cache",
    "referer": "https://apphkdm470.digitalmaker.asia.pwcinternal.com/"
}

import csv
import os
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open('Book2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(len(row),row)
        #payload = getpayLoad(row[0],row[1],row[2])
        print(payload)
        r = requests.post(url, data=json.dumps(payload), headers=headers,verify=False)
        print(r.content)
        time.sleep(3)



r = requests.post(url, data=json.dumps(payload), headers=headers,verify=False)
print(url, headers,len(json.dumps(payload)))
print(r.content)