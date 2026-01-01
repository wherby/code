# https://atcoder.jp/contests/abc437/tasks/abc437_e
# 家族树
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


def resolve():
    N =int(input())
    g = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        a,b= list(map(lambda x: int(x),input().split()))
        g[a].append((b,i))
    ans = []

    '''
    current_ids: 具有相同值的列表
    '''
    def dfs(current_ids):
        current_ids.sort()
        for idx in current_ids:
            ans.append(idx)
        
        to= defaultdict(list)
        for idx  in current_ids:
            for b,next_idx in g[idx]:
                to[b].append(next_idx)
        for b in sorted(to.keys()):
            dfs(to[b])
    dfs([0])
    ret = [str(a) for a in ans[1:]]
    return " ".join(ret)
    

def op(caseidx):
    cnt = resolve()
    print(str(cnt))


op(0)