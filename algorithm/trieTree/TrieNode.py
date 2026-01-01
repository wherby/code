# https://atcoder.jp/contests/abc437/tasks/abc437_e
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
# filename = "input/warm_up_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=False

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f

from collections import defaultdict,deque
import sys
sys.setrecursionlimit(100000)
class node:
    def __init__(self) :
        self.child ={}
        self.record = []

def resolve():
    N =int(input())
    NPtr={}
    
    Nlist= [node()]
    NPtr[0] = Nlist[0]
    cur = 0
    dic =defaultdict(int)
    for i in range(1,N+1):
        a,b= list(map(lambda x: int(x),input().split()))
        #print(b,NPtr[a].child,dic)
        if b not in NPtr[a].child:
            cur +=1 
            Nlist.append(node())
            NPtr[i]= Nlist[cur]
            dic[i]=cur
            NPtr[a].child[b] = Nlist[cur]
            #print(NPtr[a].child,"aa",b,a)
        else:
            NPtr[i] = NPtr[a].child[b]
            #print("**",i)
        NPtr[i].record.append(i)
    ret = []
    def dfs(a):
        nonlocal ret 
        a.record.sort()
        #print(a.record,a)
        ret.extend(a.record)
        for k in sorted(list(a.child.keys())):
            dfs(a.child[k])
    dfs(Nlist[0])
    ret = [str(a) for a in ret]
    return " ".join(ret)
    

def op(caseidx):
    cnt = resolve()
    print(str(cnt))


op(0)