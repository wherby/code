#https://codeforces.com/gym/103536/problem/A
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
import sys
input = sys.stdin.readline

def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s) - 1]))
def invr():
    return list((map(int,input().split())))

dp_before =[0]*10
dp_cur = [0]*10
pls =[]

def cost(i,j):
    return pls[j]-pls[i]

def compute(l,r,optl,optr):
    if l > r:
        return 
    mid = (l+r) >>1 
    best = (10**30,-1)
    for k in range(optl,min(mid,optr) +1):
        best = min(best,((dp_before[k-1] if k !=0 else 0) + (pls[mid+1]-pls[k])*(mid-k+1),k))
    dp_cur[mid] = best[0]
    opt = best[1]
    compute(l,mid-1,optl,opt)
    compute(mid+1,r,opt,optr)

def resolve():
    global pls,dp_before,dp_cur
    n,m= tuple(list(map(lambda x: int(x),input().split())))
    dp_before= [0]*n
    dp_cur =[0]*n
    ls = []
    for _ in range(n):
        ls.append(inp())

    pls=[0]*(n+1)
    for i in range(n):
        pls[i+1] =pls[i] + ls[i]

    for i in range(n):
        dp_before[i]= pls[i+1]*(i+1)

    for i in range(1,m):
        compute(0,n-1,0,n-1)
        dp_before = list(dp_cur)
        #print(dp_before,dp_cur)
    #print(dp_before)
    return dp_before[n-1]
    


ret= resolve()
print(ret)
    