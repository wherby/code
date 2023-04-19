#https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad7cf

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
    ls = input().split(" ")
    n = int(input())
    strs = []
    for _ in range(n):
        strs.append(input())
    dirs= {}
    isG =True
    for s1 in strs:
        ret =""
        for a in s1:
            ret += ls[ord(a) -ord("A")]
        if ret in dirs:
            isG = False
        dirs[ret] =1 
    if isG:
        return"NO"
    else:
        return "YES"
    #return ret
    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)