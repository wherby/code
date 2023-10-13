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

def find(ls,tar):
    n = len(ls)
    l,r =0,n-1
    cnt =0 
    while l<r:
        if ls[l] + ls[r] == tar:
            cnt +=1
            l+=1
            r -=1
        elif ls[l] + ls[r] > tar:
            r -=1
        else:
            l+=1
    return cnt

def resolve():
    N = int(input())

    ls = list(map(lambda x: int(x),input().split()))
    if N ==1:
        return 1
    ls.sort()
    ret = 10**10
    cand= [ls[0]+ls[-1],ls[1]+ls[-1],ls[0]+ls[-2],ls[1]+ls[-2]]
    for c in cand:
        if find(ls,c)==N-1:
            #print(find(ls,c),ls,c)
            if c*N - sum(ls) >0:
                ret = min(ret,c*N - sum(ls))    
    return ret if ret!=10**10 else -1

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)