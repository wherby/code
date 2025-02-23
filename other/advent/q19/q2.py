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


from functools import cache

pps = []


def find(s):
    n  = len(s)
    #print(s,pps)
    @cache
    def dfs(i):
        if i ==n:
            return 1
        ret = 0
        for p in pps:
            if len(p)<= n-i and s[i:i+len(p)] == p:
                ret += dfs(i+len(p))
        return ret
    #print(dfs(0))
    re =dfs(0)
    dfs.cache_clear()
    #print(re)
    return re


def solve():
    global pps
    ps = input()
    ps=ps.split(",")
    ps = [a.strip() for a in ps]
    ps = filter(lambda a: len(a) >0, ps)
    ps =list(ps)
    print(ps)
    pps=ps
    input()
    ls=[]
    a = input()
    while len(a)>1:
        ls.append(a)
        a = input()
    cnt = 0
    for s in ls:
        #print(find(s))
        cnt +=find(s)
    print(cnt)
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    