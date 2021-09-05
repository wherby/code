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


def getNum(ls):
	num =0 
	stat =0
	n = len(ls)
	for i in range(n):
		t= ls[i]
		if stat == 0:
			if t == '1':
				stat = 1
		elif stat == 1:
			if t == '0':
				stat =2
			elif t =='1':
				stat =1
			else:
				stat =0
		elif stat == 2:
			if t == '1':
				stat = 1
				num = num +1
			elif t =='0':
				pass
			else:
				stat = 0
	print num


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	ls=  ins[index+i]
	getNum(ls)