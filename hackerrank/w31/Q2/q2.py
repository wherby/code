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


def getOrd(ls):
	n = len(ls)
	od = [0] *n
	for i in range(1,n):
		od[i] = ls[i] -ls[i-1]
	isOrd = True
	sm=0
	for i in range(1,n):
		sm =sm +od[i]
		if od[i] <0 and od [i-1] <0:
			isOrd = False
		if od[i] < 0 and od[i] != -1:
			isOrd = False
		if od[i] >0 :
			if ls[i] != i and ls[i] != i +1:
				isOrd = False
	if isOrd == True:
		print "Yes"
	else:
		print "No"
	##print od
			




q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	ls= map(int , ins[index+i*2 +1].strip().split())
	getOrd(ls)