filename = "input01.txt"
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

m,n = map(int , ins[0].strip().split())
al = []
for i in range(m):
	t= 0
	al.append(t)
dic={"000":0}
cmds=[]
gx=0
for i in range(n):
	tp=ins[i+1].strip().split()
	tp1=[int(x) for x in tp[0:-1]]
	ar=bytearray(tp[-1])
	tp1.append(ar)
	cmds.append(tp1)

def fun1(x):
	global dic
	dic["000"] =x


def fun2(x):
	global gx, dic
	dic["000"] = dic["000"] ^x


def fun3():
	global gx, dic
	
	print dic["000"]



cmdindex=0
ix=0
def isAllOne(ar):
	for i in range(len(ar)):
		if ar[i] ==49:
			return False
	return True

def isContain(x,y):
	for i in range(len(x)):
		if y[i] ==49:
			if x[i] != 49:
				return False
	return True

def preReplay(cmds,cmdindex,ix,bitm):
	idx= ix
	while idx >=cmdindex:
		cmd =cmds[idx]
		if cmd[0] == 1 and isContain(cmd[2],bitm):
			return idx
		idx = idx -1
	return cmdindex

def replay(cmds,cmdindex,ix,bitm):
	cmdindex = preReplay(cmds,cmdindex,ix,bitm)
	dic["000"]=0
	i1= cmdindex
	while i1<=ix:
		cmd =cmds[i1]
		if cmd[0] ==1 and isContain(cmd[2],bitm):
			fun1(cmd[1])
		if cmd[0] == 2 and isContain(cmd[2],bitm):
			fun2(cmd[1])
		if cmd[0] ==3 and i1 ==ix:
			fun3()
		i1= i1+1


while(ix<len(cmds)):
	cmd = cmds[ix]
	if cmd[0] == 1 and isAllOne(cmd[2]):
		cmdindex = ix
	if cmd[0] == 3:
		replay(cmds, cmdindex, ix,cmd[1])
	ix = ix +1
