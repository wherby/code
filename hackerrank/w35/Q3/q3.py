filename = "input/input25.txt"
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

H,W = map(int , ins[0].strip().split())
index=1
mx=[]
for i in range(H):
	ls= map(int , ins[index+i].strip().split())
	mx.append(ls)
total =H*W *2
for i in range(H):
	for j in range(W):
		if i ==0:
			total = total + mx[i][j]
		else:
			total = total + abs(mx[i][j]- mx[i-1][j])
		if i == H-1:
			total = total + mx[i][j]
for j in range(W):
	for i in range(H):
		if j ==0:
			total = total + mx[i][j]
		else:
			total = total + abs(mx[i][j]- mx[i][j-1])
		if j == W-1:
			total = total + mx[i][j]
print total
