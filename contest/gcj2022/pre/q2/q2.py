#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b
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
    ls =[]
    for _ in range(3):
        #a = input()
        #print(a)
        tl = list(map(lambda x :int(x),input().split(" ")))
        ls.append(tl)
    mls =[0]*4
    for i in range(4):
        mls[i] = min(ls[0][i],ls[1][i],ls[2][i])
    if sum(mls)<10**6:
        return "IMPOSSIBLE"
    else:
        res =10**6
        ret=["0"]*4
        for i in range(4):
            ret[i] = min(mls[i],res)
            res -= ret[i]
        ret = map(lambda x: str(x),ret)
        return " ".join(ret)

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)