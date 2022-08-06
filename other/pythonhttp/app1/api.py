import http.client
import os
import configparser


import os
import ssl
import json
from collections import defaultdict,deque

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

config = configparser.RawConfigParser()
config.read("./api.cfg")
csrf = config["CIDRSTAG"]["CSRF"]
cookie = config["CIDRSTAG"]["COOKIE"]
#print(csrf,cookie)


def getJob(job):
    conn = http.client.HTTPSConnection("cidr-stg.asia.pwcinternal.com")
    headers ={"PLAY_CSRF_TOKEN":csrf,"PLAY_SESSION":cookie}
    conn.request("GET","/api/v2/job/" + job+"/status","",headers)
    response = conn.getresponse()
    #print(response.status, response.reason)
    data = response.read()
    #print(data)
    jdata = json.loads(data)
    #print(jdata)
    return jdata


def getProject(id):
    conn = http.client.HTTPSConnection("cidr-stg.asia.pwcinternal.com")
    headers ={"PLAY_CSRF_TOKEN":csrf,"PLAY_SESSION":cookie}
    conn.request("GET","/api/v2/project/" + id+"/jobs/id","",headers)
    response = conn.getresponse()
    #print(response.status, response.reason)
    data = response.read()
    jdata = json.loads(data)
    return jdata

def dfsjobs(jobID,ret):
    js = getJob(jobID)
    lss =[]
    for a in js:
        processName = a["processorStatus"]["classType"]
        start =a["processorStatus"]["startTime"]
        end = a["processorStatus"]["endTime"]
        lss.append({"name":processName,"start":start,"end":end})
    ret.append({jobID:lss})
    #print(ret)
    return ret

    

#jobs =getProject("4375")

#getJob("7adf93fc-ebb1-47f0-bac1-375dbcda2458")
projectID = [str(i) for i in range(4383,4403)]
#projectID =["4375"]
lss=[]
for id in projectID:
    allJobs  = getProject(id)
    for job in allJobs:
        try:
            lss = dfsjobs(job,lss)
        except:
            pass
print(len(lss))
with open("data.json",'w') as f:
    json.dump(lss,f)



# def processRecord(lss):
#     dic =defaultdict(list)
#     print(lss[0])
#     for ls in lss:
#         for record in ls.values():
#             print(record)

# processRecord(lss)

