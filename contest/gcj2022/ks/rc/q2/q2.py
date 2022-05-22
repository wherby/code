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


import math
def resolve():
    ret =[]
    n,a,b = tuple(list(map(lambda x: int(x),input().split())))
    sm = (1+n)*n //2
    t = math.gcd(a,b)
    a,b = a//t,b//t
    if sm %(a+b) !=0 or sm < a+b:
        return ret
    remains = sm *a //(a+b)
    for i in range(n,0,-1):
        if remains >= i:
            ret.append(i)
            remains -=i
    return ret
    
def op(caseidx):
    ret= resolve()
    ret = list(map(lambda x:str(x),ret))
    if len(ret) ==0:
        print("Case #"+str(caseidx+1)+": " + "IMPOSSIBLE")
    else:
        print("Case #"+str(caseidx+1)+": " + "POSSIBLE")
        print(str(len(ret)))
        print(" ".join(ret))
    

for i in range(int(input())):
    op(i)