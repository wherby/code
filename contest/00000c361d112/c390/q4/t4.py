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
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +(ord(s1[i]) - ord('a')+1))%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        dic = defaultdict(SortedList)
        for idx,word in enumerate(wordsContainer):
            n = len(word)
            hs = StringHash(word)
            for i in range(n+1):
                dic[hs.query(i,n)].add((n,idx))
        ret = []
        for word in wordsQuery:
            n = len(word)
            hs = StringHash(word)
            for i in range(n+1):
                if hs.query(i,n) in dic:
                    ret.append(dic[hs.query(i,n)][0][1])
                    break
        return ret



re =Solution().stringIndices(wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"])
print(re)