#
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
def generateN(n):
    ls = []
    sm = 0
    mn = 3*n
    for i in range(n-1):
        ls.append(n+i)
        sm += 3*n+i
    start = int(math.sqrt(sm))
    for j in range(start+3*n,7*n):
        t = j - 3*n
        if t*t - sm >= 4*n:
            ls.append(t*t-sm)
            break
    #print(len(ls))
    return ls

def resolve():

    n = int(input().split()[0])
    ls = generateN(n)
    ret= " ".join([str(a) for a in ls])
    print(ret)
    #return ret
    
    

def op(caseidx):
    resolve()
    #print("Case #"+str(caseidx+1)+": " + ret)
    

for i in range(int(input())):
    op(i)