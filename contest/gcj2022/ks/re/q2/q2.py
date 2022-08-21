#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
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

# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from bisect import bisect_right,insort_left


def resolve():
    
    n, = tuple(list(map(lambda x: int(x),input().split())))
    ls1  = list(map(lambda x: int(x),input().split()))
    ret = [-1]*n
    ls2 = [(a,i) for i,a in enumerate(ls1)]
    ls2.sort()
    for i,a in enumerate(ls1):
        a2 = a*2
        k = bisect_right(ls2,(a2,100000))
        #print(a,ls2[k-1],k)
        if ls2[k-1][0]>a2: continue
        if ls2[k-1][1] == i:
            k = k-1
        if k-1 ==-1:continue
        ret[i] = ls2[k-1][0]
    ret = [str(i) for i in ret]
    return str(" ".join(ret))
    
def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)