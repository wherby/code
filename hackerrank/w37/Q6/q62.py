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
CONST = 1000000007

def exponenX(base,exponent):
    global CONST 
    if base == 1:
        return 1
    result =1
    while exponent >0:
        if exponent &1:
            result=result *base % CONST
        exponent =exponent >>1
        base =base **2 %CONST
    return result



def generate(ls,ran):
    res = []
    for x in ran:
        for y in ls:
            t = list(y)
            t.append(x)
            res.append(t)
    return res

def getlen(ls,subls):
    n = len(subls)
    cnt = 0
    for i in range(n):
        if ls[i] != subls[i]:
            return cnt
        cnt = cnt +1
    return cnt

def getMaxLen(ls):
    n = len(ls)
    MX =0
    for i in range(1,n):
        if ls[i] == ls[0]:
            tpmx = getlen(ls,ls[i:])
            if tpmx >MX:
                MX = tpmx
    return MX



n,k= map(int , ins[0].strip().split())
if n >2 :
    ls = [[0]]
    ran = range(k)
    for i in range(n-1):
        ls = generate(ls,ran)
    lenls =[getMaxLen(x) for x in ls]
    print sum(lenls)*len(ran)
else:
    a= exponenX(k,n-1) *(n-1 )% CONST
    print a




