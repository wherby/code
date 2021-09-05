#https://www.hackerrank.com/contests/w35/challenges/matrix-land/submissions/code/1304212460
#If input lines are too large, record inputs will course Running time Error

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

def getMaxLin(ls,upls):
	m =len(ls)
	msl = [0]*(m+2)
	msr= [0]*(m+2)
	re = [0]*m
	tp =[0]*m

	for j  in range(1,m+1):
		msl[j] = max(msl[j-1] + ls[j-1],0)
	for j in range(1,m+1):
		idx = m+1-j
		msr[idx] =max(msr[idx+1 ] +ls[idx-1],0)

	tp[0]=upls[0] + ls[0]
	re[0] =tp[0] + msr[2]
	for i in range(1,m):
		tp[i] = max(tp[i-1] + ls [i] , upls[i] + ls[i] + msl[i])
		re[i] = tp[i] + msr[i+2]
	#print "XXX"
	#print re
	tp[m-1] =upls[m-1] + ls[m-1]
	re[m-1] = max(re[m-1],tp[m-1] + msl[m-1])
	for i in range(1,m):
		idx = m-1-i
		tp[idx] = max(tp[idx +1] + ls[idx] , upls[idx] +ls[idx]+ msr[idx+2])
		re[idx] = max(re[idx],tp[idx] + msl[idx])
	#print tp
	return re 
 




n,m = map(int , ins[0].strip().split())
index=1
MX =[]
MX1 = []
for i in range(n):
	##If input lines are too large, record inputs will course Running time Error
	ls= map(int , ins[index+i].strip().split())
	MX.append(ls)

upls = [0]*m
for i in range(n):
	ls =MX[i]
	msl = [0]*(m+2)
	msr= [0]*(m+2)
	re = [0]*m
	tp =[0]*m

	for j  in range(1,m+1):
		msl[j] = max(msl[j-1] + ls[j-1],0)
	for j in range(1,m+1):
		idx = m+1-j
		msr[idx] =max(msr[idx+1 ] +ls[idx-1],0)

	tp[0]=upls[0] + ls[0]
	re[0] =tp[0] + msr[2]
	for i in range(1,m):
		tp[i] = max(tp[i-1] + ls [i] , upls[i] + ls[i] + msl[i])
		re[i] = tp[i] + msr[i+2]
	#print "XXX"
	#print re
	tp[m-1] =upls[m-1] + ls[m-1]
	re[m-1] = max(re[m-1],tp[m-1] + msl[m-1])
	for i in range(1,m):
		idx = m-1-i
		tp[idx] = max(tp[idx +1] + ls[idx] , upls[idx] +ls[idx]+ msr[idx+2])
		re[idx] = max(re[idx],tp[idx] + msl[idx])
	upls = re



print max(re)

#print GetMaxLinkedLine(MX[1],1)



