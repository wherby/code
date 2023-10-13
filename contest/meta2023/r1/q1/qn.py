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


def verify(mid,ls):
    n = len(ls)
    for i in range(1,n-1):
        if ls[i]-ls[i-1] > mid and ls[i+1]-ls[i] > mid:
            return False
    if ls[1]-ls[0]> mid or ls[-1] -ls[-2] > mid:
        return False
    return True
    

def resolve():
    N = int(input())
    ls = list(map(lambda x: int(x),input().split()))
    ls.sort()
    l,r = 0, ls[-1]
    mid = 0
    while l < r:
        mid = (l+r)>>1
        #print(l,r,mid,verify(mid,ls))
        if verify(mid,ls):
            r=mid 
        else:
            l =mid+1
    left,right = 0,0
    for i in range(N-2):
        if N== 5:
            print(i,ls[i]- ls[0],l)
        if ls[i]- ls[0]<=l:
            left = (ls[i]+ls[0]) /2
    for i in range(N-1,1,-1):
        if ls[-1] -ls[i] <= l:
            right = (ls[i] + ls[-1])/2
    print(right,left,l)
    return right -left

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)