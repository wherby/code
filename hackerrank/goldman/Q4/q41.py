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


inp=[]
try:
  while True:
    inp.extend(map(int,raw_input().split()))
except:
  pass

def getPrice(v1):
	global time,value,n,valueOrd
	i = bisect.bisect_left(valueOrd,v1)
	if i <n:
		print  time[i]
	else:
		print  -1

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

n,q =inp[0],inp[1]
time = inp[2:2+n]
value = inp[2+n:2+2*n]
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
base=2+2*n
for i in range(q):
	ls= [inp[base+2*i],inp[base+2*i+1]]
	getAns(ls[0],ls[1])