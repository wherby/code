import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

mod = 16777216



def swq(secret):
    re= (secret*64 ^ secret)%mod
    re = ((re //32   )^re)%mod 
    re = (re*2048 ^re)%mod
    #print(secret,re)
    return re

# se =123
# for _ in range(10):
#     se =swq(se)
from collections import defaultdict,deque

def solve():
    ls=[]
    a = input()
    sm = 0
    dic = defaultdict(int)
    for _ in range(2002):
        ls.append(int(a))
        a = int(a)
        tmp=[]
        vls = []
        for _ in range(2000):
            b =swq(a)
            tmp.append( b%10-a %10)
            vls.append(b%10)
            a =b
        sm+=a
        a = input()
        s1 ={}
        for i in range(3,2000):
            t1 = tuple(tmp[i-3:i+1])
            c = vls[i]
            if t1 not in s1:
                s1[t1] =c
                dic[t1] +=c 

         
    print(max(dic.values()))
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    