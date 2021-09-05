#https://www.hackerrank.com/contests/w23/challenges/commuting-strings
filename = "input/input02.txt"
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


def getLastRepeat(rps,fstr,st):
	next = getNext(st)
	mx= max(next) +1
	rps=rps[1:]
	rps= [fstr +i for i in rps]
	lst=""
	rpn= len(rps)
	for i in range(1,mx+1):
		crps=rps[0:i]
		lst="".join(crps)
		cn=st.split(lst) 
		if (len(cn)-1) *i ==rpn and len(''.join(cn))==0:
			break
	return lst

def findRepeat1(st):
	next = getNext(st)
	mx= max(next) +1
	print next
	lst = st[0:mx]
	cn=st.split(lst) 

	if (len(cn)-1) *mx ==len(st) and len(''.join(cn))==0:
		return lst
	return st[0:1]

def getNext(st):
	l1=len(st)
	next=[0]*l1
	next[0] = -1
	k = -1
	j =0
	while j < l1-1:
		if k ==-1 or st[j] ==st[k]:
			k = k + 1
			j = j +1
			next[j] = k
		else:
			k=next[k]
	return next

#https://www.hackerrank.com/contests/w23/challenges/commuting-strings/editorial
#get min repeated string in string
def getNextMin(st):
	l1=len(st)
	next=[0]*l1
	k = 0
	i =0
	j=0
	n = len(st)
	while i < l1-1:
		i = i +1
		while j and st[i] != st[j]:
			j=next[j-1]
		if st[i] == st[j]:
			j =j +1
		next[i] =j
	while  n %(n-j):
		j = next[j-1]
	k = n -j 
	return k


def findRepeat(st):
	re=[]
	fstr=st[0]
	rps=st.split(fstr)
	lst = getLastRepeat(rps,fstr,st)
	return lst

st, = map(str , ins[0].strip().split())
nstr, = map(long , ins[1].strip().split())
#lst=findRepeat1(st)

#print (nstr/len(lst))%(10**9+7)
print (nstr/getNextMin(st))%(10**9+7)


