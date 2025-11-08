# https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/B?source=facebook
# 
# 为什么会OT? 因为在路径遍历的时候，从 X 可以跳跃到 X+1，X+2，X+3，。。X+M 点，然后又在各自点上遍历此点开始的长度为L的段，这样就构成了 N**2 复杂度，然后每个新的值也要经历此过程 就构成了N**3 复杂度
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/hash_slinger_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

FILEDEBUG=True
if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f


from heapq import heapify,heappop,heappush 
from collections import defaultdict,deque
def resolve():
    N,M = list(map(lambda x: int(x),input().split()))
    nums = list(map(lambda x: int(x),input().split()))
    g = [[] for _ in range(N+2)]

    for i,a in enumerate(nums):
        cur = 0
        for j in range(i,N):
            cur =(cur+nums[j])%M 
            g[i+1].append((j+2,cur))
    vis= [10**20]*M*2
    cand = [(0,0,0)]

    vis[0] = 0
    while cand:
        idx,value,fr =heappop(cand)
        if vis[value] <fr:
            continue
        vis[value] = fr
        if fr ==idx:
            for j in range(idx+1,N+2):
                heappush(cand,(j,value,fr))
        #vis[value]=idx
       # print(cand)
        for j,v2 in g[idx]:
            nv = (v2^value)
            #print(j,nv,value)
            if vis[nv]> j and nv != value:
                vis[nv] = j 
                heappush(cand, (j,nv,j))
    cnt = 0
    for i in range(M*2):
        if vis[i] <= N+2:
            cnt +=1
    #print(vis)
    return cnt


def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)