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



from math import inf

class node:
    def __init__(self) -> None:
        self.child ={}
        self.max =-inf
        self.min = inf
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = node()
    
    def insert(self,w):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            if i not in r.child:
                r.child[i] = node()
            r = r.child[i]
        r.max = max(r.max,w)
        r.min = min(r.min,w)
        r.is_end = True
    
    def get(self,x):
        r =self.root
        if len(r.child) == 0:
            return -1
        ls = '{:032b}'.format(x)
        for i in ls:
            i = int(i)
            if i not in r.child:
                print(r.child,1-i)
                r= r.child[1-i]
            else:
                r = r.child[i]
        return r.max
    

Mod =998244353

def resolve():

    inp = int(input())
    ls =[]
    for _ in range(inp):
        ls.append(input())
    tre =Trie()

    return ""

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)