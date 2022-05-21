#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
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

import math
def calcN1(n):
    ans =0
    nn = (n+0.5)*(n+0.5)
    for i in range(-n,n+1):
        y = math.floor(math.sqrt(nn-i**2))
        ans +=y*2+1
    return ans
    
def calcN2(n):
    ans = 0
    for r in range(1,n+1):
        ans += calcC(r)
    return ans *4+1
    
def calcC(r):
    xt =round(math.sqrt(r**2/2))
    yt = round(math.sqrt(r**2 - xt**2))
    xxt = min(xt,yt)
    return xxt*2 +1 if xt!=yt else xxt*2

def resolve():
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    n= ls[0]
    x1=calcN1(n)
    x2=calcN2(n)
    return x1-x2

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + str(ret))
    
    

for i in range(int(input())):
    op(i)
    