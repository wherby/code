from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c))
        visit = defaultdict(deque)
        presum = [0]*(n+1)
        depth ={}
        depth[-1] = 0 
        mx = -1
        mxl =-1
        lastGood = [0]
        def dfs(a,p,c):
            nonlocal mx,mxl
            depth[a] = depth[p] +1 
            #print(depth[a],a,presum,p,c)
            #print(presum[depth[a]])
            presum[depth[a]]=presum[depth[p]] +c 
            visit[nums[a]].append(depth[a])
            if len(visit[nums[a]]) ==1:
                lastGood.append(lastGood[-1])
            else:
                dd= max( visit[nums[a]][-2],lastGood[-1])
                lastGood.append(dd)
                

            b = lastGood[-1]
            t = presum[depth[a]] -presum[b+1]
            if t > mx:
                #print(t,visit[nums[a]],presum,a,p,c,visit[nums[a]])
                mx = t 
                mxl = depth[a] - b 
            elif t == mx and mxl > depth[a] - b:
                mxl = depth[a] - b
            for b,c in g[a]:
                if b != p:
                    dfs(b,a,c)
            visit[nums[a]].pop()
            lastGood.pop()
        dfs(0,-1,0)
        return [mx,mxl]





#re =Solution().longestSpecialPath(edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], nums = [2,1,2,1,3,1])
#re =Solution().longestSpecialPath(edges =[[1,0,7],[1,2,4]], nums = [1,1,3])

re =Solution().longestSpecialPath(edges = [[1,0,8]], nums = [2,2])
print(re)