#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin



        

def cnt1(n):
    cnt =0
    for i in range(n*2+1):
        for j in range(n*2+1):
            if (i-n)**2 + (j-n)**2<=n**2:
                cnt +=1
    return cnt
def cnt2(n):
    dic ={}
    for k in range(n+1):
        for i in range(k*2+1):
            j= round(math.sqrt(k**2 - (i-k)**2))
            dic[(i-n,j)]=1
            dic[(i-n,-j)]=1
    print(dic)
    return len(dic)

def resolve():
    ls = input().split(" ")
    ls = [int(x) for x in ls]
    n= ls[0]
    t1 = cnt1(n)
    t2 = cnt2(n)
    print(t1,t2)
    return t1-t2
    

def op(caseidx):
    ret= resolve()
    
    print("Case #"+str(caseidx+1)+": " + str(ret))
    
    

for i in range(int(input())):
    op(i)
    

# 2 4 6
# 8 10 12 14