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


def moreCandyOrMoreWorker(candyLeft,workerMchine):
	global per
	worker,machine = workerMchine
	wds = candyLeft / (worker * machine)
	wdsWith =(candyLeft +per) / (max(worker,machine)*(min(worker,machine)+1))
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

	return (workerMchine,candyHave,candyLeft)
	


m,w,per,n = map(int , ins[0].strip().split())
turn =0
workerMchine = (m,w)
candyHave=0
candyLeft =n
ct=0
while candyHave <n:
	ct = ct +1
	candyHave = candyHave + w *m
	candyLeft = n - candyHave
	if candyHave > n:
		break
	workerMchine,candyHave,candyLeft = moreWorkerMachine(workerMchine,candyHave,candyLeft)
	#print workerMchine,candyHave,candyLeft
	w,m = workerMchine


print ct