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
    random.shuffle(tls)
    a,b = i1[0],i1[1]
    ls[a] = b
    cnt = 0
    start =1
    while cnt < (k//2):        
        for i in range(start,n+1):
            if ls[i] == -1:
                start =i+1
                break
        print("T " + str(i))
        i1 = list(map(lambda x: int(x),input().split()))
        a,b = i1[0],i1[1]
        ls[a] =b
        cnt +=1
    start =0
    while cnt < k :        
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
    ret =[]
    for i in range(1,n+1):
        if ls[i] != -1:
            visited +=1
            sm += ls[i]
            ret.append(ls[i])
    
    guess = int(sm /visited *n/2)
    print("E "+str(guess))
    
def op(caseidx):
    resolve()
    

for i in range(int(input())):
    op(i)