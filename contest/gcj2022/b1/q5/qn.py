#https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


import random
def resolve():
    i1 = list(map(lambda x: int(x),input().split()))
    n,k = i1[0],i1[1]
    ls = [-1]*(n+1)
    i1 = list(map(lambda x: int(x),input().split()))
    tls = [i for i in range(1,n+1)]
    random.shuffle(tls)
    g = [[] for _ in range(n+1)]
    a,b = i1[0],i1[1]
    ls[a] = b
    cnt = 0
    start =0
    while cnt < k :
        if (b >= 2 and len(g[a])*2 < b)  :
            a1 = a
            print("W")
            i1 = list(map(lambda x: int(x),input().split()))
            a,b = i1[0],i1[1]
            ls[a] =b
            g[a1].append(a)
            g[a].append(a1)
        else:
            for i in range(start,n):
                if ls[tls[i]] == -1:
                    start =i+1
                    break
            print("T " + str(tls[i]))
            i1 = list(map(lambda x: int(x),input().split()))
            a,b = i1[0],i1[1]
            ls[a] =b
        cnt +=1
    visited =0
    sm = 0
    muti =0
    sig =0
    for i in range(1,n+1):
        if ls[i] != -1:
            visited +=1
            sm += ls[i]
            if ls[i]>2:
                muti +=1
            else:
                sig +=1
    if muti *2 >sig:
        guess = n + min(int(((sm-sig *2)  * n /(muti *2) )) ,0)
    else:
        guess = n + min(int((sm * n /(visited *2) -n)) ,0)//4
    print("E "+str(guess))
    
def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)