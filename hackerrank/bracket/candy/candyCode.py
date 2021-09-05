filename = "input/input00.txt"
f=open(filename,'r')
# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/openbracket/challenges/making-candies/submissions/code/7470551

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def moreCandyOrMoreWorker(candyLeft,workerMchine):
	global per
	worker,machine = workerMchine
	wds = (candyLeft+ worker*machine-1) / (worker * machine)
	wdsWith =(candyLeft +per +(max(worker,machine)*(min(worker,machine)+1)) -1) / (max(worker,machine)*(min(worker,machine)+1))
	if wds >= wdsWith:
		return False
	else:
		return True

def moreWorkerMachine(workerMchine, candyHave,candyLeft):
	global per
	worker,machine = workerMchine

	while not moreCandyOrMoreWorker(candyLeft,workerMchine) and candyHave >= per:
		candyLeft =candyLeft +per
		candyHave = candyHave -per
		workerMchine = (max(worker,machine),min(worker,machine)+1)
		worker,machine = workerMchine
		if min (worker,machine) > per:
			cn = candyHave/per
			candyLeft = candyLeft + per *cn
			candyHave = candyHave -per *cn
			if cn < abs(worker - machine):
				workerMchine = (max(worker,machine),min(worker,machine)+cn)
				worker,machine = workerMchine
			else:
				df =abs(worker - machine)
				x1 =(cn-df)/2

				workerMchine = (max(worker,machine) + x1 + (cn-df)%2,max(worker,machine) + x1 )
				worker,machine = workerMchine

	return (workerMchine,candyHave,candyLeft)
	


m,w,per,n = map(int , ins[0].strip().split())
turn =0
workerMchine = (m,w)
candyHave=0
candyLeft =n
ct=0
CCN =0
while candyHave <n and CCN <1000:
	CCN =CCN +1
	perDay=w *m
	if (per -candyHave) / perDay > 1:
		if candyLeft >per:
			CC =per - candyHave
		else:
			CC = candyLeft
		rr = CC / perDay 
		ct =ct +rr
		candyHave = candyHave + perDay * rr
		candyLeft = candyLeft - perDay -rr
	else:
		ct = ct +1
		candyHave = candyHave + w *m

		candyLeft = n - candyHave
	if candyHave >= n:
		break
	workerMchine,candyHave,candyLeft = moreWorkerMachine(workerMchine,candyHave,candyLeft)
	#print ct,workerMchine,candyHave,candyLeft

	# if candyHave > per and moreCandyOrMoreWorker(candyLeft,workerMchine):
	# 	ct= ct + (candyLeft + perDay -1) /perDay
	# 	break

	#print workerMchine,candyHave,candyLeft
	#print ct,workerMchine,candyHave
	w,m = workerMchine


print ct