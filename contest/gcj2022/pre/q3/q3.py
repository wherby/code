#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
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
    ls.sort()
    left,right =0,0
    mx = 0
    for i in range(n):
        a = ls[i]
        right +=1
        while a < right-left:
            left +=1
        mx = max(mx,right -left)
    return mx

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)