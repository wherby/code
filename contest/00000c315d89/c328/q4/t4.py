from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

def TreeMaxPath(g,root):
    n  = len(g)
    visit =[0]*n
    d =[0]*n
    ans=0
    def dfs(x):
        nonlocal ans
        visit[x] = 1
        for y,c in g[x]:
            if visit[y] : continue
            dfs(y)
            ans = max(ans,d[x] + d[y] +c)
            d[x] = max(d[x], d[y] + c )

    dfs(root) # The node is root node<= hard code and only applied to one root tree
    #print(d)
    return ans

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g=  [[] for _ in range(n)]
        ind = [0]*n
        for a,b in edges:
            g[a].append((b,price[b]))
            g[b].append((a,price[a]))
            ind[a] +=1
            ind[b] +=1
        root = -1
        mx = 10**9
        for i in range(n):
            if ind[i] ==1 and price[i]<mx:
                root = i 
                mx = price[i]
        ret =0
        def dfs(node,acc,anotherNode):
            nonlocal ret
            for i in g[node]:
                
                ret =max(ret,acc + dfs(i,acc+ price[node],anotherNode))
                
        return ret




#re =Solution().maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5])
# 2-0-1-3
# 1 2 3 1
#re =Solution().maxOutput(4,[[2,0],[0,1],[1,3]],[2,3,1,1])
re = Solution().maxOutput(6,[[0,1],[1,2],[1,3],[3,4],[3,5]],[9,8,7,6,10,5])
print(re)