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



n,k = map(int , ins[0].strip().split())
ls =  map(int , ins[1].strip().split())

mskls = [0]*n
def getN(ls, index):
    global n,k,mskls
    startValue = ls[index] - k*(index ) 
    ps = [startValue] * n
    for i in range(n):
        ps[i] = ps[i] + k*i
    cnt = 0

    for i in range(n):
        if ps[i] == ls[i]:
            mskls[i] =1
        else:
            cnt = cnt +1
    return cnt

minN = n 
for i in range(n):
    if mskls[i] ==0:
        cnt = getN(ls,i)
        if cnt <minN:
            minN = cnt
print minN

