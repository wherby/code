#https://codeforces.com/contests/1726
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
    n,= tuple(list(map(lambda x: int(x),input().split())))
    ls= list(map(lambda x: int(x),input().split()))
    if n <=1:
        return 0
    mx = ls[-1]-ls[0]
    #print(ls,n)
    mx = max(mx,max(ls[1:]) -ls[0],ls[n-1]-min(ls[:n-1]))
    ls= ls +ls 
    for i in range(n):
        mx = max(mx,ls[i]-ls[i+1])
    return mx
    

def op(caseidx):
    ret= resolve()
    print(ret)
    

for i in range(int(input())):
    op(i)