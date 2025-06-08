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
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        @cache
        def minOp(s1,s2):
            diff = defaultdict(int)
            for a,b in zip(s1,s2):
                if a != b:
                    diff[(a,b)] +=1
            keys = list(diff.keys())
            cnt = 0
            for key in keys:
                while diff[key]>0 and diff[key[::-1]] >0:
                    diff[key] -=1
                    diff[key[::-1]] -=1
                    cnt +=1
                cnt += diff[key]
            #print(s1,s2,cnt ,diff)
            return cnt

        @cache
        def dfs(i):
            if i ==-1:
                return 0 
            ret = 10**10
            for j in range(i,-1,-1):
                t1 = word1[j:i+1]
                t2 = word2[j:i+1]
                t3 = t1[::-1]
                ret = min(ret, dfs(j-1) + min(minOp(t1,t2),minOp(t2,t3)+1))
                #print(t1,t2,t3, min(minOp(t1,t2),minOp(t2,t3)),ret,minOp(t1,t2),minOp(t2,t3))
            #print(ret)
            return ret
        return dfs(n-1)
            




re =Solution().minOperations(word1 = "abcdef", word2 = "fedabc")
print(re)