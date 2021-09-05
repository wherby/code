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
index=1
nls =[]
for i in range(q):
	name,price = ins[index+i].strip().split()
	nls.append([name,price])

def filterPr(price):
	n = len(price)
	if n == 0:
		return False
	num4=0
	for i in price:
		if i != "4" and i !="7":
			return False
		if i =="4":
			num4 = num4 +1
	if n%2==0 and n/2 == num4:
		return True
	return False
nls = filter(lambda x: filterPr(x[1]),nls)
nls = sorted(nls, key = lambda x : int(x[1]))

if len(nls) >=1:
	print nls[0][0]
else:
	print -1