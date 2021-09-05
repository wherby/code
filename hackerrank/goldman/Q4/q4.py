filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/gs-codesprint/challenges/time-series-queries
import math
import sys
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def getPrice(v1):
	global time,value,n,valueOrd
	i = bisect.bisect_left(valueOrd,v1)
	if i <n:
		print  time[i]
	else:
		print -1

def getTime(v1):
	global n,time,value,valuereOrd
	idx =bisect.bisect_left(time,v1)
	if idx <n:
		print valuereOrd[idx]
	else:
		print -1




def getAns( t1,v1):
	if t1 == 1:
		getPrice(v1)
	else:
		getTime(v1)

n,q = map(int , ins[0].strip().split())
time = map(int , ins[1].strip().split())
value = map(int , ins[2].strip().split())
valueOrd= [0]*n
maxv =0
for i in range(n):
	maxv = max(maxv,value[i])
	valueOrd[i] = maxv
valuereOrd = [0]*n
maxrv =0
for i in range(n):
	maxrv = max(maxrv,value[n-1-i])
	valuereOrd[n-1-i] = maxrv
index=3
for i in range(q):
	ls= map(int , ins[index+i].strip().split())
	getAns(ls[0],ls[1])