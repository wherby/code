filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

ls=[]
lls=[]

def addT(ls,lls,st):
	lls.append(copy.deepcopy(ls))
	for i in range(len(st)):
		ls.append(st[i])
	return (ls,lls)
def reT(ls,lls,n):
	lls.append(copy.deepcopy(ls))
	for i in range(n):
		ls.pop()
	return (ls,lls)
def prT(ls,n):
	print ls[n-1]

def undo(ls,lls):
	return lls.pop()

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n= map(str , ins[index+i].strip().split())
	if n[0]=="1":
		ls,lls=addT(ls,lls,n[1])
	if n[0]=="2":
		ls,lls=reT(ls,lls,int(n[1]))
	if n[0]=="3":
		prT(ls,int(n[1]))
	if n[0]=="4":
		ls = undo(ls,lls)


#https://www.hackerrank.com/challenges/simple-text-editor

