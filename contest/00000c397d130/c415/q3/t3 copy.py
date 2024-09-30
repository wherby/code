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


class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dp = [10**10] * (n+1)
        dp[0] = 0
        dic ={}
        for word in words:
            hs = StringHash(word[::-1])
            m = len(word)
            for i in range(m):
                dic[hs.query(i,m)] =1

        mx = max(len(a) for a in words)
        hs = StringHash(target[::-1])
        for i in range(1,n+1):
            for j in range(1,min(i,mx)+1):
                if hs.query(i-j,i) in dic:
                    dp[i] = min(dp[i],dp[i-j] +1)
                else:
                    break
        #print(dp)
        return dp[-1] if dp[-1]<10**10 else -1




re =Solution().minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")
print(re)