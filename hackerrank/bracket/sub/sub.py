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


dic1={}

def initDic():
	global dic1
	for i in range(1,51):
		dic1[i]=0

def addToDic(n):
	global dic1
	if n in dic1:
		dic1[n] = dic1[n] +1
	else:
		dic1[n] =1

def getDic(ls):
	initDic()
	for i in ls:
		addToDic(i)

def ValidX(n):
	global ls

	return n

def resoveRe(re):
	if re[0][0]==1:
		return re[0]
	else:
		mx = ValidX(re[0][0])
		mxV = re[0]
		m = len(re)
		for i in range(1,i):
			if m> re[i][1]:
				break
			else:
				t1 = ValidX(re[i][0])
				if t1 > mx:
					mx =t1
					mxV=re[i]
		return rev



def reSolve(ls):
	global n,dic1
	getDic(ls)
	re = []
	for i in range(1,n+1):
		re.append([i,dic1[i]])
	sorted(re,key=lambda x : x[1])
	re1= resoveRe(re)
	print re1[1],re1[0]





q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i*2].strip().split())
	ls = map(int , ins[index+i*2 +1].strip().split())
	reSolve(ls)
	