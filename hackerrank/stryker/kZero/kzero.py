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



def serch1(num):
	global lst,zlist
	n1= len(zlist)
	if n1 <num:
		print "NO"
	else:
		print zlist[num-1]

def change1(index,num):
	global lst,zlist
	if lst[index] ==0:
		zlist.remove(index)
	if num ==0 and lst[index] !=0:
		zlist.append(index)
		zlist= sorted(zlist)
	lst[index]=num



m,n= map(int , ins[0].strip().split())
lst = map(int , ins[1].strip().split())
zlist=[]
for i in range(m):
	if lst[i] ==0:
		zlist.append(i)

index=2
for i in range(n):
	q1= map(int , ins[index+i].strip().split())
	if q1[0]==1:
		serch1(q1[1])
	if q1[0]==2:
		change1(q1[1],q1[2])

