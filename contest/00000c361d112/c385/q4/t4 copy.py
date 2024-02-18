from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf



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
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        cnt = 0 
        for word in words:
            m = len(word)
            sh= StringHash(word)
            for i in range(1,m+1):
                if sh.query(0,i) == sh.query(m-i,m):
                    #print("a")
                    cnt += dic[sh.query(0,i)]
            dic[sh.query(0,m)] +=1 
        return cnt




re =Solution().countPrefixSuffixPairs(["a","a"])
print(re)