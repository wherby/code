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
    ls = list(map(lambda x: int(x),input().split()))
    r,c = ls[0],ls[1]
    #print(r,c)
    cnt = 0 
    res =[]
    for i in range(2*r+1):
        if i %2 ==0:
            if i ==0:
                tp = ".." + "+-"*(c)
            else:
                tp = "+-"*(c+1)
        else:
            if i ==1:
                tp = ".." + "|."*(c)
            else:
                tp= "|."*(c+1)
        tp1=tp[:len(tp)-1]
        print(tp1)
    return res

def op(caseidx):
    print("Case #"+str(caseidx+1)+": ")
    resolve()

for i in range(int(input())):
    op(i)