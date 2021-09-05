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
    ins.append(line.strip())
n, = map(int , ins[0].strip().split())

al = []
for i in range(n):
	al.append(ins[1+i])

ds=[]

dic = {}



def updateDS(ds):
	global dic
	a=ds[-1][0]
	lds=len(ds)
	if lds >1:
		n = ds[-2][1]
	else:
		return
	sa = a == ds[-2][0]
	re = a == ds[0][0]
	if n!=0:
		while a != ds[n][0]  and n >0:
			n= ds[n][2]
	if a ==ds[n][0]:
		ds[-1][1] = n+1
		if not sa:
			ds[n][2] = ds[n-1][2] +1
		else:
			ds[n][2] = ds[n-1][2]
		if re:
			ds[n][2]=0
	else:
		ds[-1][1]=0

 
def fun(s,ds):
	if s[0] == '+':
		t1=s.split()
		a = int(t1[1])
		ds.append([a,0,0])
		updateDS(ds)
	if s[0]=="-":
		x = ds[-1][0]
		ds =ds[:-1]
	return ds


def prfun(ds):
	lds=len(ds)
	if lds <1:
		print 0
		return
	print ds[-1][1]


for i in range(len(al)):
	ds= fun(al[i],ds)
	#print ds
	prfun(ds)
	