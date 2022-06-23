# https://www.irs.gov/e-file-providers/foreign-country-code-listing-for-modernized-e-file

import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

inputFile = "input.txt"
f=open(inputFile,'r')
lines = []
for line in f:
    line= line.replace('\n',"")
    line = line.split('\t')
    lines.append(line)
res = []
for a in lines:
    tmp = "\"" + a[0].lower() +"\""  + "->" + "\"" + a[1] + "\""
    res.append(tmp)
print(",".join(res))