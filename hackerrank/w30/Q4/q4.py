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


def findMin(ls):
	n = len(ls)
	mx= ls[n-1][0] * ls[n-1][1]
	idx = 0
	for i in range(1,n):
		#print i
		tp = (ls[i][0] -ls[i-1][0]) * ls[i][1]
		#print  tp,mx
		if tp < mx:
			mx = tp
			idx = i
		
	return (idx,mx)

def adjust(ls,i):
	ls[i-1][1] = ls[i-1][1] + ls[i][1]
	del ls[i]
	return ls

num,k= map(int , ins[0].strip().split())
index=1
ls =[]
for i in range(num):
	h,n= map(int , ins[index+i].strip().split())
	ls.append([h,n])
mm=0
n = num -k
for i in range(n):
	j,tp = findMin(ls)
	#print j,tp

	mm = mm + tp
	ls = adjust(ls,j)
	#print ls

print mm







	