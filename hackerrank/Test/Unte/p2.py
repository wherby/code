#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
a=len(s)
b=len(t)
if a + b <= k:
    print "Yes"
else:
    abmin= min(a,b)
    n=0
    for i in range(abmin):
        if s[i] == t[i]:
            n = n +1
        else:
            break
    re =k - ( a + b -i *2 )
    if re >= 0 and re %2 ==0:
    	print "Yes"
    else:
    	print "No"