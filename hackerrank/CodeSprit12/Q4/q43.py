filename = "input/input00.txt"
f=open(filename,'r')

#https://www.hackerrank.com/contests/world-codesprint-12/challenges/factorial-array
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

mem =[-1]*50


def factorial(n):
    global mem
    if n <=1 :
        mem[n]=1
        return 1
    MOD =10**9
    if mem[n] != -1:
        return mem[n]
    else:
        mem[n]= n * factorial(n-1) %MOD
        return mem[n]
    
for i in range(0,50):
    factorial(i)


def addls(l,r):
    global ls,validls,dic1
    start = bisect.bisect_left(validls,l)
    end = bisect.bisect_right(validls,r)
    # for i in range(l,r+1):
    #     ls[i] = ls [i]+1
    removeIndex = []
    for i in range(start,end):
        tp = validls[i]
        dic1[tp] = dic1[tp] +1
        if dic1[tp] >= 49:
            removeIndex.append(i)
    for i in range(len(removeIndex)):
        k = removeIndex[i]
        validls.pop(k-i)



def change(i,v):
    global ls,validls,dic1
    start = bisect.bisect_left(validls,i)
    if len(validls)> start and validls[start] == i:
        if v <= 49:
            dic1[i] = v
        else:
            dic1[i] = v
            validls.pop(start)
    else:
        if v <=49:
            dic1[i] =v
            bisect.insort_left(validls,i)

def sumls(l,r):
    global mem,validls,dic1
    start = bisect.bisect_left(validls,l)
    end = bisect.bisect_right(validls,r)
    re = 0
    for i in range(start,end):
        tp = validls[i]
        if dic1[tp] <= 49:
            re  = re + mem[dic1[tp]]
    re = re % 10**9
    print re#,validls,dic1


n,q = map(int , ins[0].strip().split())
index=2
ls =[0]
ls1 = map(int , ins[1].strip().split())
ls.extend(ls1)
validls = []
dic1 = {}
for i in range(1,n+1):
    if ls[i] <= 49:
        validls.append(i)
        dic1[i] =ls[i]
#print validls,dic1
#print mem[:10]
for i in range(q):
    cmd,l,k= map(int , ins[index+i].strip().split())
    if cmd ==1:
        addls(l,k)
    if cmd ==2:
        sumls(l,k)
    if cmd ==3:
        change(l,k)