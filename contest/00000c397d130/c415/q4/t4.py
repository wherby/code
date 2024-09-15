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



from typing import List, Tuple, Optional
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.n = n
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

    def search(self,pattern):
        m = len(pattern)
        ps = StringHash(pattern)
        ph = ps.query(0,m)
        ret = []
        for i in range(self.n-m+1):
            if self.query(i, i+ m) == ph:
                ret.append(i)
        return ret

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:





re =Solution()
print(re)