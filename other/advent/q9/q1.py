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


def solve():
    ls = input()
    print(len(ls))
    n = len(ls)
    ls = [int(a) for a in ls]
    sm = sum(ls)
    print(sm)
    tls = [-1]*sm
    cur=0
    for i in range(n):
        if i%2 ==0:
            for j in range(ls[i]):
                tls[cur] = i//2
                cur +=1
        else:
            for j in range(ls[i]) :
                cur +=1
    l,r = 0,sm-1
    while l <=r:
        while tls[l] != -1:
            l +=1
        while tls[r] ==-1:
            r -=1
        if tls[l] == -1 and tls[r]!= -1 and l <=r:
            tls[l] = tls[r]
            tls[r] =-1

    print(l,r,tls[l-10:l+20])
    acc =0
    #print(tls)
    for i,a in enumerate(tls):
        if a >=0:
            acc += i*a 
    print(acc)

    


solve()