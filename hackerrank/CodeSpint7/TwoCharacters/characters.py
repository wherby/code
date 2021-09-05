#https://www.hackerrank.com/contests/world-codesprint-7/challenges/two-characters
filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

def getSameChar(ls):
	rc = ls[0]
	n = len(ls)
	for i in range(1,n):
		t = ls[i]
		if t ==rc:
			return rc
		rc=t
	return -1

def filterChar(ls,c):
	rls= filter(lambda x: x!=c,ls)
	return rls



q, = map(int , ins[0].strip().split())
ls = ins[1].strip()
cc=getSameChar(ls)
while cc != -1:
	ls =filterChar(ls,cc)
	if len(ls) <1:
		break
	cc =getSameChar(ls)

n=len(ls)
dic={}
for i in range(n):
	t=ls[i]
	if t in dic:
		dic[t]=dic[t]+1
	else:
		dic[t]=1
keys=dic.keys()
keyPair=[]
for k1 in keys:
	for k2 in keys:
		if k1 !=k2:
			keyPair.append(min(k1,k2)+max(k1,k2))
keyPair=set(keyPair)
removed=set()
for k12 in keyPair:
	k1=k12[0]
	k2=k12[1]
	if abs(dic[k1]-dic[k2])>1:
		removed.add(k12)

keyPair =keyPair -removed

mx=0
def testPair(keyPair,ls):
	k1=keyPair[0]
	k2=keyPair[1]
	n = len(ls)
	state=0
	for i in range(n):
		t=ls[i]
		if t==k1 or t==k2:
			if state ==0:
				if t==k1:
					state=1
				else:
					state=2
			else:
				if state == 1:
					if t == k1:
						return 0
					else:
						state=2
				else:
					if t == k1:
						state =1
					else:
						return 0
	tp=filter(lambda x: x == k1 or x ==k2, ls)
	return len(tp)
for pair in keyPair:
	n1= testPair(pair,ls)
	if n1 > mx:
		mx=n1
print mx


