# 对每一段和的dp可以向左扩展，这样就可以使得组合方式都只有一种，没有跳过某段的方式，这样也可以维护右端点
# 因为可以维护到达某个值的最小右端点
# 所以可以把最小右端点的这个值作为搜索起点
# 然后用类似Dijstra 算法，因为在访问图的时候，是增加此端点的右端点，所以选择未访问的点的最小右端点是成立的。
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
    dp = [[10**10]*(N+2) for _ in range(M)]
    minRight= [10**20]*M*2
    for i,a in enumerate(nums):
        cur = 0
        for j in range(i,N):
            cur =(cur+nums[j])%M 
            g[i+1].append((j+2,cur))
            dp[cur][i+1] = j+2
            minRight[cur] = min(minRight[cur],j+2)
    for i in range(M):
        for j in range(N,-1,-1):
            dp[i][j] = min(dp[i][j], dp[i][j+1])
    minRight[0] = 0 
    vis = {}
    while True:
        #find  minRight not visit
        x = -1 
        mnR = N+3
        for i in range(M*2):
            if i in vis:
                continue
            if minRight[i] < mnR:
                x = i 
                mnR = minRight[i]
        if x == -1:
            break
        vis[x] = 1 
        for j in range(M):
            nx = x^j
            if minRight[nx] > dp[j][mnR]:
                minRight[nx] = dp[j][mnR]
    return len(vis)
    
    


def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)