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

mem =[-1]*100
AllSm =-1

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
    
for i in range(0,100):
    factorial(i)


def addls(l,r):
    global ls,AllSm,mem

    for i in range(l,r+1):
        ls[i] = ls [i]+1
    if AllSm != -1:
        for i in range(l,r+1):
            if ls[i] <99:
                AllSm = AllSm + mem[ls[i]] - mem[ls[i] -1]

def getMem(v):
    global mem
    if v <99:
        return mem[v]
    return 0

def change(i,v):
    global ls,AllSm
    if AllSm != -1:
        AllSm = AllSm + getMem(v) - getMem(ls[i])
    ls[i] =v


def sumls(l,r):
    global mem,ls,AllSm
    if AllSm ==-1:       
        re = 0
        for i in range(l,r+1):
            if ls[i] < 99:
                re  = re + mem[ls[i]]
        re = re % 10**9
        AllSm =re
        print re
    else:
        print AllSm


n,q = map(int , ins[0].strip().split())
index=2
ls =[0]
ls1 = map(int , ins[1].strip().split())
ls.extend(ls1)
#print mem[:10]
for i in range(q):
    cmd,l,k= map(int , ins[index+i].strip().split())
    if cmd ==1:
        addls(l,k)
    if cmd ==2:
        sumls(l,k)
    if cmd ==3:
        change(l,k)