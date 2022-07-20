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

def midLs(ls):
    if len(ls) ==0:
        return 0
    k = len(ls)//2
    if len(ls)%2 ==1:
        return ls[k]
    else:
        return (ls[k]+ ls[k-1])/2

def resolve():
    n,m = tuple(list(map(lambda x: int(x),input().split())))
    ls = list(map(lambda x: int(x),input().split()))
    ls.sort()
    ret =0
    ls1 = ls[:n-m+1]
    #print(ls1)
    ret = midLs(ls1)
    for a in ls[n-m+1:]:
        ret +=a 
    return str(ret)
    

def op(caseidx):
    ret= resolve()
    print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)