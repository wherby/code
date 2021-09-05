filename = "input/input04.txt"
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


al8=[i*8 for i in range(125) ]



dic8 ={}
for a in al8:
	dic8[a]=1

def getN(start):
	global dic8,ls
	tp = ls[start:start+1]
	tp = int (tp)
	cnt = 0
	if tp  in dic8:
		cnt = cnt +1
	if start > 0:
		tp = ls[start-1:start+1]
		tp = int(tp)
		if tp in dic8:
			cnt = cnt+1
	if start > 1:
		tp = ls[start-2:start+1]
		tp = int(tp)
		if tp in dic8:
			cnt =cnt  + start-1
	return cnt




def modpow(a,b):
	global CONSTPRIME
	if b ==0:
		return 1
	if b == 1:
		return a
	if b %2 == 1 :
		return a * modpow(a,b-1) % CONSTPRIME
	k = modpow(a, b /2)
	return (k*k)%CONSTPRIME

def getNumber(start):
	global dic8,ls
	cnt = 0
	lastw= ls[start]
	tp = int (lastw)
	if tp ==0 or tp == 8:
		cnt = cnt +1
	if tp %2 !=0:
		return 0
	for i in range(start):
		midw = ls[i]
		tp = int(lastw) + int(midw) *10
		if tp in dic8 :
			cnt = cnt +1
		for j in range(i):
			fstw = ls[j]
			tp = int(lastw) + int(midw) *10 + 100 * int(fstw)
			if tp in dic8:
				cnt = cnt + modpow(2,j)
	return cnt

numList=[]
for i in range(10):
	numList.append([])

def count2List(lst1,lst2):
	cnt = 0
	for l1 in lst1:
		for l2 in lst2:
			if l1 > l2:
				cnt = cnt +1
	return cnt

def count3List(lst1,lst2,lst3):
	cnt = 0
	for l1 in lst1:
		for l2 in lst2:
			for l3 in lst3:
				if l1 > l2  and l2 >l3:
					cnt = cnt + modpow(2, l3)
	return cnt

def getNumberAll():
	global dic8,numList
	cnt = 0
	for i in range(10):
		ls1 =numList[i]
		if i in dic8:
			cnt = cnt + len(ls1)
		for j in range(10):
			ls2 = numList[j]
			tp = i + j * 10
			if tp in dic8:
				cnt = cnt + count2List(ls1,ls2)
			for k in range(10):
				ls3 = numList[k]
				tp = i + j * 10 + k * 100
				if tp in dic8:
					cnt = cnt + count3List(ls1,ls2,ls3)

	return cnt % CONSTPRIME



CONSTPRIME = 1000000007
n, = map(int , ins[0].strip().split())
ls, =  ins[1].strip().split()

for i in range(n):
	tp = int(ls[i])
	numList[tp].append(i)


#print sum(ln) %CONSTPRIME
print getNumberAll()