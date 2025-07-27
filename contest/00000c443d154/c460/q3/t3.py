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


def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        mx = max(nums)
        pms = get_prime(mx)
        n = len(nums)
        g = [[] for _ in range(n)]
        for i in range(n-1):
            g[i].append(i+1)
            g[i+1].append(i)
        for i,a in enumerate(nums):
            if a in pms:
                for j in range(a,mx+1,a):
                    for b in dic[j]:
                        g[i].append(b)
        
        st = deque([[0,0]])
        visit = {}
        while st:
            idx,step = st.popleft()
            if idx == n-1:
                return step
            if idx in visit:
                continue
            visit[idx]= step 
            for b in g[idx]:
                if b not in visit:
                    st.append((b,step+1))





re =Solution().minJumps([7,5,7])
print(re)