# https://leetcode.cn/contest/weekly-contest-419/problems/count-the-number-of-winning-sequences/submissions/572270955/
# DFS ot

from typing import List, Tuple, Optional
import sys
sys.setrecursionlimit(1500000)

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
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)
        dic = {"F":0,"W":1,"E":2}
        @cache
        def dfs(i,acc,lst):
            if i == n:
                if acc >0:
                    return 1 
                return 0 
            if acc + n-i<0:
                return 0
            ret =0
            for a in "FWE":
                if a != lst:
                    if a == s[i]:
                        ret+= dfs(i+1,acc,a)
                    elif ((dic[a] +3)-dic[s[i]])%3 ==1:
                        ret += dfs(i+1,acc +1,a)
                    else:
                        ret += dfs(i+1,acc -1 ,a)
            return ret%mod
        return dfs(0,0,"a")%mod





re =Solution().countWinningSequences("FWEFW"*200)
print(re)