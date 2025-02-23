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

se =123
for _ in range(10):
    se =swq(se)


def solve():
    ls=[]
    a = input()
    sm = 0
    for _ in range(2002):
        ls.append(int(a))
        a = int(a)
        for _ in range(2000):
            a =swq(a)
        sm+=a
        a = input()
    print(sm)
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    