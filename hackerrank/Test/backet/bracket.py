f = open('input/input18.txt')
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
ss=[]
q, = map(int , ins[0].strip().split())
index =1
mx=0
inl=set(['{','[','('])
outl=set([']','}',')'])
dic ={'(':')','[':']','{':'}'}

for i in range(q):
	ls=[]
	inorder=True
	t,=map(str , ins[index+i].strip().split())
	for j in range(len(t)):
		t1= t[j]
		if t1 in inl:
			ls.append(t1)
			#print ls
		else:
			if len(ls)==0:
				inorder=False
				break
			t2 = ls.pop()
			#print t2
			if t1 != dic[t2]:
				inorder=False
				break
	if len(ls)!=0:
		inorder=False
	if inorder == True:
		print "YES"
	else:
		print "NO"