filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w31/challenges/zero-one-game
#Status machine
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



#status: 0=0 1=1 01 = 2 00 =3 10=4 11=5

def getNum(ls):
	n = len(ls)
	num = 0
	status =0
	pending = 0
	if ls[0] == 1:
		status =1
	else:
		status = 0
	for i in range(1,n):
		t = ls[i]
		if t ==0:
			if status ==0:
				status = 3
			elif status ==1:
				status =4
			elif status == 2:
				num = num +1
				status =3
				if pending == 1:
					num = num +1
					pending =0
			elif status == 3:
				num = num +1
				status =3
				if pending == 1:
					num = num +1
					pending =0
				
			elif status == 4:
				status =3
				if pending == 1:
					num = num +1
					pending =0
			elif status==5:
				status =4
				if pending == 1:
					num = num +1
					pending =0
		if t ==1:
			if status ==0:
				status =2
			elif status == 1:
				status =5
			elif status ==2:
				status=5
				pending = 0
			elif status == 3:
				status=2
				pending = 1
			elif status == 4:
				status =2
				pending=0
			elif status == 5:
				status =5
				pending =0
	return num






q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	ls= map(int , ins[index+i*2+1].strip().split())
	n= getNum(ls)
	if n%2 ==0:
		print "Bob"
	else:
		print "Alice"