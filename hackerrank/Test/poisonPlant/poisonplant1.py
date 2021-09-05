filename = "input/input01.txt"
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
ls= map(int , ins[1].strip().split())

re=[]
minL=ls[0]
re.append([minL,0])
maxday=0
#days=0
for i in range(1,q):
	days=0
	t1=ls[i]
	if t1<minL:
		minL=t1
	if t1>ls[i-1]:
		days=1

	while len(re)>0 and re[-1][0]>= t1:
		if t1>minL:
			if days> (re[-1][1]+1):
				days=days
			else:
				days=re[-1][1]+1
		re.pop()
	if maxday>days:
		maxday=maxday 
	else:
		maxday=days
	re.append([t1,days])
print maxday



#https://www.hackerrank.com/challenges/poisonous-plants
