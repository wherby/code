import http.client
import os
import configparser


import os
import ssl
import json
from collections import defaultdict,deque
import traceback

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
    #print(job)
    #print("==" *100)
    #print(job, data)
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
    try:
        js = getJob(jobID)
        lss =[]
        #print(jobID,js)
        for a in js:
            #print(a)
            processName = a["processorStatus"]["classType"]
            end = a["processorStatus"]["endTime"]
            start = end 
            if "startTime" in a["processorStatus"]:
                start =a["processorStatus"]["startTime"]
            lss.append({"name":processName,"start":start,"end":end})
            if "subJobid" in a["processorStatus"]:
                jls = a["processorStatus"]["subJobid"]
                for j in jls:
                    #print(j,jls)
                    ret=dfsjobs(j,ret)
        ret.append({jobID:lss})
        #print(ret)
    except :
        pass
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
        except Exception as e:
            traceback.print_exc()
            #print(str(e))
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

