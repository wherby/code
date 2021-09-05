filename = "input/input04.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Sqrt Decomposition, MO's Algorithm
# https://www.hackerrank.com/contests/w31/challenges/nominating-group-leaders/problem    only pass in pypy3
import math
import sys
import bisect 
import functools

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

MAXV = 1000000000008
SQ = 320  #squre of whole

def cmpMo(p1,p2):
    global SQ
    if p1[0] // SQ > p2[0]//SQ:
        return -1
    if p1[0] // SQ < p2[0] //SQ:
        return 1
    if p1[1]   < p2[1] :
        return 1
    else:
        return -1

def addFreq(i,freq,Dec,vls):
    global SQ
    Dec[vls[i] // SQ][freq[vls[i]]] = Dec[vls[i] // SQ][freq[vls[i]]] -1
    freq[vls[i]] =freq[vls[i]]  +1
    Dec[vls[i] // SQ][freq[vls[i]]] =Dec[vls[i] // SQ][freq[vls[i]]] +1


def decFreq(i,freq,Dec,vls):
    global SQ
    Dec[vls[i] // SQ][freq[vls[i]]] =Dec[vls[i] // SQ][freq[vls[i]]] -1
    freq[vls[i]] =freq[vls[i]]  -1
    Dec[vls[i] // SQ][freq[vls[i]]] =Dec[vls[i] // SQ][freq[vls[i]]] +1

def search(z,Dec,freq,ans,num):
    global SQ,m
    for ii in range(m // SQ +2):
        if Dec[ii][z] > 0:
            for j in range(SQ):
                tj = ii *SQ  + j
                if freq[tj] == z:
                    ans[num] = tj
                    break
            break

def MoSearchWithSqureComp(vls,qls):
    global m,MAXV,SQ,q
    ans = [MAXV] *q 
    Dec = []
    for i in range(m//SQ +2):
        Dec.append([0]*(m+2))
    #print(Dec)
    freq = [0]*(m+SQ)

    qls =  sorted(qls, key=functools.cmp_to_key(cmpMo))
    L = qls[0][0]
    R = qls[0][1]
    z = qls[0][2]
    num = qls[0][3]
    for i in range(L,R+1):
        addFreq(i,freq,Dec,vls)
    search(z,Dec,freq,ans,num)
    for i in range(1,q):
        l = qls[i][0]
        r = qls[i][1]
        while L < l:
            decFreq(L,freq,Dec,vls)
            L = L +1
        while R > r:
            decFreq(R,freq,Dec,vls)
            R =R-1
        while L>l:
            L = L -1
            addFreq(L,freq,Dec,vls)
        while R <r:
            R= R +1
            addFreq(R,freq,Dec,vls)
        z = qls[i][2]
        num =qls[i][3]
        search(z,Dec,freq,ans,num)
    for i in ans:
        if i == MAXV:
            print(-1)
        else:
            print(i)
    #print(Dec,)
    #print(freq)
    #print(vls[l:R+1])


n, = map(int , ins[0].strip().split())
index=1
for i in range(n):
    m, =  map(int , ins[index+0].strip().split())
    vls= list(map(int , ins[index+1].strip().split()))
    q, = map(int , ins[index+2].strip().split())
    qls =[]
    for j in range(q):
        l,r,z = map(int , ins[index+3 + j].strip().split())
        qls.append([l,r,z,j])
    index = index + q +3
    #print(qls)
    MoSearchWithSqureComp(vls,qls)
