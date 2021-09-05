#https://www.hackerrank.com/contests/w23/challenges/commuting-strings
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


def getLastRepeat(rps,fstr,st):
	rps=rps[1:]
	rps= [fstr +i for i in rps]
	lst=""
	rpn= len(rps)
	for i in range(1,rpn+1):
		crps=rps[0:i]
		lst="".join(crps)
		cn=st.split(lst) 
		if (len(cn)-1) *i ==rpn and len(''.join(cn))==0:
			break
	return lst


def findRepeat(st):
	re=[]
	fstr=st[0]
	rps=st.split(fstr)
	lst = getLastRepeat(rps,fstr,st)
	return lst

st, = map(str , ins[0].strip().split())
nstr, = map(long , ins[1].strip().split())
lst=findRepeat(st)

print (nstr/len(lst))%(10**9+7)