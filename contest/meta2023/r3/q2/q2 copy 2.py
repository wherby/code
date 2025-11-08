import resource
import sys

# Set maximum memory limit to 10 GB (in bytes)
# 10 GB = 10 * 1024 * 1024 * 1024 bytes
MAX_MEMORY = 20 * 1024 * 1024 * 1024 

try:
    # Set the soft and hard limits
    resource.setrlimit(resource.RLIMIT_AS, (MAX_MEMORY, MAX_MEMORY))
except (ValueError, resource.error) as e:
    print(f"Could not set memory limit: {e}")
    print("This method may not be fully supported on macOS.")

# Your main Python code follows...
print("Memory limit set, running script...")
# 

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

FILEDEBUG=False
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
    vis= [10**20]*M*2
    cands = [[] for _ in range(N+2)]
    cands[0].append((0,0))
    for i,a in enumerate(nums):
        cur = 0
        for j in range(i,N):
            cur =(cur+nums[j])%M 
            if vis[cur]>j:
                vis[cur] =j
                cands[j].append((cur,j))
            g[i+1].append((j+2,cur))
    
    #print("finish step 1 ")
    
    vis[0] = 0
    for i in range(N+2):
        for value,fr in cands[i]:
            if vis[value] <fr:
                continue
            vis[value] = fr
            if i +1 <N+2:
                cands[i+1].append((value,fr))
            #vis[value]=idx
        # print(cand)
            for j,v2 in g[i]:
                nv = (v2^value)
                #print(j,nv,value)
                if vis[nv]> j and nv != value:
                    vis[nv] = j 
                    cands[j].append((nv,j))
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