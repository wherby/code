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



n,q= map(int , ins[0].strip().split())


dic1={1:1,2:2,3:3}

def hacnacci(n):
	if n ==0:
		return 0
	global dic1
	if n in dic1:
		return dic1[n]
	else:
		b=hacnacci(n-1) + 2*hacnacci(n-2) + 3*hacnacci(n-3)
		dic1[n] = b %2
		return b %2
# ls= range(100 +2)
# ls2=map(hacnacci,ls)
# print ls2

def getOdd(n):
	if n == 1:
		return 1
	ls4=[0,1,0,0,1,1,1]
	return ls4[(n-2)%7]


map1 = []
map2=[]
map3=[]
map4=[]
for i in range(n):
	tp = [0]*n
	tp2 = [0]*n
	tp3 = [0]*n
	tp4 = [0]*n
	map1.append(tp)
	map2.append(tp2)
	map3.append(tp3)
	map4.append(tp4)
for i in range(1,n+1):
	for j in range(1,n+1):
		t1 = (i*j)**2
		# t2= ((n+1 -j) *(i))**2  
		# t3= ((n+1 -i) *(n+1-j)) **2
		# t4= ((j) *(n+1-i)) **2
		if getOdd(t1)%2 ==1:
			map1[i-1][j-1]=1
			map2[n-j][i-1]=1
			map3[n-i][n-j]=1
			map4[j-1][n-i]=1
		# if getOdd(t2)%2 ==1:
		# 	map2[i-1][j-1]=1
		# if getOdd(t3)%2 ==1:
		# 	map3[i-1][j-1]=1
		# if getOdd(t4)%2 ==1:
		# 	map4[i-1][j-1]=1
# print map1
# print map2
# print map3
# print map4
ls5=[0]*4
maps=[map1,map2,map3,map4]
for k in range(4):
	mapT= maps[k]
	cnt = 0
	for i in range(n):
		for j in range(n):
			if map1[i][j] != mapT[i][j]:
				cnt= cnt+1
	ls5[k] = cnt
index=1
for i in range(q):
	r,= map(int , ins[index+i].strip().split())
	print ls5[r%360/90]


