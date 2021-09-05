#https://www.hackerrank.com/contests/stryker-codesprint/challenges/point-filtering
filename = "input/input00.txt"
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


n1=len(ins)


n,m = map(int , ins[0].strip().split())
index=1
lst=[]
cmds=[]
bucket={}
for i in range(n):
	ls=  map(str,ins[index+i].strip().split())
	lst.append([int(ls[0]),ls[1],ls[2],ls[3]])
lst=sorted(lst,key=lambda x : float(x[3]))


def findX(bucket,num):
	if num in bucket:
		t1=[str(i)  for i in bucket[num]]
		st1=",".join(t1)
		print str(num) + " = (" + st1 + ")"
	else:
		print 'Point doesn\'t exist in the bucket.'

def removeX(bucket,num):
	global lst
	if num in bucket:
		if len(lst) ==0:
			print "No more points can be deleted."
			return
		print "Point id " +str(num) + " removed."
		del(bucket[num])

		t1=lst.pop()
		bucket[t1[0]]=[t1[1],t1[2],t1[3]]
	else:
		print "Point doesn't exist in the bucket."

for i in range(m):
	t1=lst.pop()
	bucket[t1[0]]=[t1[1],t1[2],t1[3]]


for i in range(n+1,n1):
	ls1=ins[i].strip().split()

	if ls1[0].lower() == 'f':
		findX(bucket,int(ls1[1]))
	if ls1[0].lower() == 'r':
		removeX(bucket,int(ls1[1]))
