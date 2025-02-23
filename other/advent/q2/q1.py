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

from itertools import pairwise


def isGood(a,b,c):

    return  a+c*1 <=b <= a+c*3 or a+c*1 >=b >= a+c*3 


def solve():
    ls1,ls2 =[],[]
    ans = 0
    for i in range(1000):
        t = list(map(lambda x: int(x),input().split()))
        m = len(t)
        for j in range(m):
            t1 = t[:j] + t[j+1:]
            isG = False
            if all([isGood(a,b,1) for a,b in pairwise(t1)]) or all([isGood(a,b,-1) for a,b in pairwise(t1)]):
                #print(i)
                isG = True
                break
        if isG:
            ans +=1
        
    print(ans)
    


solve()