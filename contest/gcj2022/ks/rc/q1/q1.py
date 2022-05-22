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


spcial = [ "#", "@","*","&"]
def addIfNotExist(ls,a,fn):
    if any(fn(x) for x in ls):
        return ls
    else:
        return ls +a

def resolve():
    n = int(input())
    ls = input()
    ls = addIfNotExist(ls,"A",lambda x: x.isupper())
    ls = addIfNotExist(ls,"a",lambda x: x.islower())
    ls = addIfNotExist(ls,"1",lambda x: x.isdigit())
    ls = addIfNotExist(ls,"#",lambda x: x in spcial)
    if len(ls) < 7:
        ls= ls +"1"*(7-len(ls))
    return ls
    #return ret
    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)