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


from random import randint
BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*BASE +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*BASE)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        ths = StringHash(t)
        n = len(s)
        m = n//k
        dic = defaultdict(int)
        for i in range(k):
            t1 = ths.query(i*m,(i+1)*m)
            dic[t1] +=1

        shs = StringHash(s)

        for i in range(k):
            t1 = shs.query(i*m,(i+1)*m)
            if dic[t1]>0:
                dic[t1] -=1
            else:

                return False
        return True






re =Solution().isPossibleToRearrange(s = "aabbcc", t = "bbaacc", k = 3)
print(re)