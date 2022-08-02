
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

############ ---- Input Functions ---- ############
def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return list((map(int,input().split())))


def resolve():
    n,m = tuple(list(map(lambda x: int(x),input().split())))
    ls = invr()
    acc,acc2 =0,0
    ls1 =[0]*n 
    ls2 = [0]*n 
    for i in range(1,n):
        if ls[i-1]>ls[i]:
            acc += ls[i-1] -ls[i]
        ls1[i] =acc
        if ls[n-i]>ls[n-1-i]:
            acc2 += ls[n-i] - ls[n-1-i]
        ls2[n-1-i] = acc2
    ret = [0]*m
    for i in range(m):
        a,b = invr()
        a,b = a-1,b-1
        if a >b:
            ret[i] = ls2[b] -ls2[a]
        else:
            ret[i] = ls1[b] -ls1[a]
        print(ret[i])

resolve()