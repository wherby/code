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
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dp = [10**10] * (n+1)
        dp[0] = 0
        dic ={}
        for word in words:
            m = len(word)
            for i in range(1,m+1):
                dic[word[:i]]=1
        mx = max(len(a) for a in words)
        for i in range(1,n+1):
            for j in range(1,min(i,mx)+1):
                if target[i-j:i] in dic:
                    dp[i] = min(dp[i],dp[i-j] +1)
        #print(dp)
        return dp[-1] if dp[-1]<10**10 else -1




re =Solution().minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")
print(re)