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



def getNumber(q,ls,total):
	t = min(ls)
	num =0
	lsindex = sorted(range(len(ls)), key=lambda k: ls[k])
	for i in range(q):
		tindex = lsindex[i]
		t1 = ls[tindex]
		if t1 <=total:
			tn = total / t1
			total = total - t1 *min(tn,tindex +1)
			num = num + min(tn, tindex +1)
		else:
			break
	# while t<=total:

	# 	#print total
	# 	tidx = ls.index(t)
	# 	tn = total/ ls[tidx]
	# 	total = total - t * min(tn,tidx+1)
	# 	num = min(tn,tidx +1) + num
	# 	ls[tidx] = total +1
	# 	t = min(ls)
	# 	#print total,ls
	print num




q, = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
total,= map(int , ins[2].strip().split())
getNumber(q,ls,total)
