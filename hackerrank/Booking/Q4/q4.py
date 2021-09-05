filename = "input/input001.txt"
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



WDS= map(str , ins[0].strip().split())
WDS =map(lambda x:x.lower(), WDS)
WDS= set(WDS)



q, = map(int , ins[1].strip().split())
index=2
dic={}
for i in range(q):
	n,= map(int , ins[index + i*2].strip().split())
	t1 = ins[index + i*2 + 1].strip()
	t1=t1.replace("."," ")
	t1=t1.replace(","," ")
	wdT= map(str , t1.split())
	wdT = map(lambda x:x.lower(), wdT)
	if n in dic:
		dic[n].extend(wdT)
	else:
		dic[n]=wdT

re=[]
for k,v in dic.items():
	n1=0
	for v1 in v:
		if v1 in WDS:
			n1 = n1 +1
	re.append([n1,k])
re=sorted(sorted(re, key = lambda x : x[1]), key = lambda x : x[0], reverse = True)




re1= map(lambda x: str(x[1]),re)

print " ".join(re1)

