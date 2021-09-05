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


def partitian(ls,grap):
	global grapPart
	ct =0
	n = len(ls)
	for s1,e1 in grap:
		if ls[s1] ==0 and ls[e1]==0:
			ct = ct+1
		if ls[s1] !=0 and ls [e1]!= 0:
			a1= ls[s1]
			b1= ls[e1]
			if a1 != b1:
				for i in range(n):
					if ls [i] == b1:
						ls[i] = a1
		if ls[s1] ==0:
			ls[s1] = ct
		if ls [e1] == 0:
			ls[e1] = ct
	for i in range(1,ct+1):
		grapPart.append({})
	for i in range(1,n):
		t = ls[i]-1
		grapPart[t][i] =1

#generate children map
def getListDic(lstDic,grap):
	for s1,e1 in grap:
		lstDic[s1][s1]=1
		lstDic[s1][e1]=1
		lstDic[e1][e1]=1
		for dc1 in lstDic:
			if s1 in dc1:
				dc1[e1]=1



n,m,q = map(int , ins[0].strip().split())
ls= [0]*(n+1)
grapPart=[]
dic2={}
index=1
grap=[]
lstDic=[]
for i in range(n+1):
	lstDic.append({})
for i in range(m):
	s1,e1= map(int , ins[index+i].strip().split())
	grap.append((s1,e1))
grap=sorted(grap,key = lambda x: x[0])

partitian(ls,grap)
getListDic(lstDic,grap)
# print ls
# print grap
# print grapPart
#print lstDic
index = index +m
cmdLst=[]
pn = len(grapPart)
def getPartialNumber(px):
	global grapPart
	pn =len(grapPart)
	for i in range(pn):
		if px in grapPart[i]:
			return i

def printPxOnCmdHistory(cmdList,px):
	global lstDic
	n = len(cmdList)
	tmp=-1
	#print cmdList
	for i in range(n-1, -1 ,-1):
		t = cmdList[i]
		if t[0] ==1:
			if px in lstDic[t[1]]:
				if tmp > -1 and px < tmp:
					return tmp
				return t[2]
		else:
			if px in lstDic[t[1]]:
				if tmp >t[2]:
					tmp = t[2]
	return 0

for i in range(pn):
	cmdLst.append([])
for i in range(q):
	cmd =  map(int , ins[index+i].strip().split())
	px = cmd[1]
	pi = getPartialNumber(px)
	if cmd [0] ==3:
		txxx = printPxOnCmdHistory(cmdLst[pi],px)
		print txxx
	else:
		cmdLst[pi].append(cmd)

