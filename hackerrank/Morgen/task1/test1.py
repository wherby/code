f = open('input/input19.txt')
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


m,n = map(int , ins[0].strip().split())
vs =  map(int , ins[1].strip().split())

qs=[]
for i in range(n):
	t1,=map(int, ins[2+i].strip().split())
	qs.append(t1)


vd={}
for i in range(m):
	v1=vs[i]
	if v1 not in vd:
		vd[v1]=[i+1]
	else:
		vd[v1].append(i+1)
	# if v1 in vd.keys():
	# 	vd[v1].append(i+1)
	# else:
	# 	vd[v1]=[i+1]


keyList=vd.keys()


ans=[]
for i in range(n):
	a1=qs[i]
	a0=m
	a11=-1
	for j in range(len(keyList)):
		a2=keyList[j]
		a3= a2 +a1
		if a3 in vd:
			a5=vd[a2]
			a4=vd[a3]
			for z in a4:
				for y in a5:
					if z - y < a0 and z >y:
						a0=z-y
						a11=(y,z)
			
	if a0==m:
		ans.append((-1,0))
	else:
		ans.append(a11)

for i in range(len(ans)):
	a1,a2= ans[i]
	if a1 == -1:
		print a1
	else:
		a3 = str(a1) + " " + str(a2)
		print a3

