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



def resolve():
    n = int(input())
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    mn = 0
    l,r = 0,n-1
    cnt =0
    while l <= r:
        t = -1
        if ls[l] <=ls[r] :
            t = ls[l]
            l +=1
        else:
            t = ls[r]
            r -=1
        if t >=mn:
            mn = t
            cnt +=1
        else:
            pass
    return str(cnt)
    #return ret
    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)