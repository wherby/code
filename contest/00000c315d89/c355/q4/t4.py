from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i,p in enumerate(parent):
            if p >=0:
                g[p].append(i)
        sm = 0
        state =[0]*n 
        def dfs(x,pre):
            pre = pre^(1<<(ord(s[x]) - ord('a')))
            state[x] = pre
            for b in g[x]:
                dfs(b,pre)
            return 
        dfs(0,0)
        #print(state)
        dic =defaultdict(int)
        for i in range(n):
            sm += dic[state[i]]
            for j in range(26):
                sm += dic[state[i]^(1<<j)]
            dic[state[i]] +=1
        return sm



re =Solution().countPalindromePaths(parent = [-1,0,0,1,1,2], s = "acaabc")
print(re)