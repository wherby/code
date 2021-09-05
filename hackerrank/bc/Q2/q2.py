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
a=ins[0].strip()
k = int(ins[1])

al=[]
for i in range(26):
	al.append([])
n = len(a)
for i in range(n):
	t= int(ord(a[i])-ord('a'))
	al[t].append(i)
re = []
index=0
for i in range(26):
	tp = al[25-i]
	tp1 = filter(lambda x: x>=index,tp)
	if len(tp1) >= k:
		if len(tp1)>0:
			re.extend(tp1)
			index = max(tp1)

res=""
for i in re:
	res = res+a[i]
print res