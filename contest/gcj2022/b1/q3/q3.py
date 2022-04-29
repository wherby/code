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



def cost(k,j,mt):
    pass

def resolve():
    inp = list(map(lambda x :int(x),input().split(" ")))
    m,n = inp[0],inp[1]
    mt=[[0]*n]
    for i in range(m):
        inp = list(map(lambda x :int(x),input().split(" ")))
        mt.append(inp)
    sm = 0
    for i in range(1,m+1):
        

    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " )
    

for i in range(int(input())):
    op(i)