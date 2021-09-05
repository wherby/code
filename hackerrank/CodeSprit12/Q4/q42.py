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
    global ls
    for i in range(l,r+1):
        ls[i] = ls [i]+1

def change(i,v):
    global ls
    ls[i] =v

def sumls(l,r):
    global mem,ls
    re = 0
    for i in range(l,r+1):
        if ls[i] < 99:
            re  = re + mem[ls[i]]
    re = re % 10**9
    print re


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