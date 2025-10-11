# 
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



def resolve():
    inp = int(input())
    ls = list(map(lambda x: int(x),input().split()))
    n = len(ls)
    cnt = 0 
    for i in range(n-1):
        md = min(ls[i:])
        midx = ls.index(md)
        cnt += midx - i +1
        #print( ls[:i] ,ls[i:midx+1][::-1], ls[midx+1:])
        ls = ls[:i] + ls[i:midx+1][::-1]+ ls[midx+1:]
        #print(ls)
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)