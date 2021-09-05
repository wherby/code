filename = "input/input20.txt"
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


q, = map(int , ins[0].strip().split())
index=1
tls=[]
mp = []
for i in range(q):
	ls= map(int , ins[index+i].strip().split())
	mp.append(ls)

for i in range(q):
	t1=[]
	for j in range(q):
		if j !=i:
			if mp[i][j] !=0:
				t1.append(j)
	k =len(t1)
	for j in range(k):
		for l in range(k):
			x1 = t1[j]
			x2 =t1[l]
			if x1 !=x2:
				if mp[x1][x2] !=0:
					mmm = sorted([i,x1,x2])
					tls.append((mmm[0],mmm[1],mmm[2]))
tls= set(tls)
#print mp
#print tls

def numInSet(t,tset):
	num =0 
	for i in t:
		if i in tset:
			num = num +1
	return num

def updateSet(tset,tls):
	isUpdate= False
	for t in tls:
		num = numInSet(t,tset)
		#print num
		if num == 2:
			isUpdate = True
			for x in t:
				if x not in tset:
					tset.add(x)
	return isUpdate



mxset=set()
mxnum =0
for x in tls:
	tset = set(x)
	isUpdate =updateSet(tset,tls)
	while isUpdate:
		isUpdate =updateSet(tset,tls)
	if mxnum < len(tset):
		mxnum = len(tset)
		mxset =tset
print len(mxset)
re = ""
re =map(lambda x:x+1, mxset)
re  = map(str, re)
re = " ".join(re)
print re 

