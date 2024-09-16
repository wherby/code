# https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/
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
        mxl = max(len(word) for word in words)
        lenHset = [set() for _ in range(mxl)]
        for word in words:
            hs = StringHash(word)
            m = len(word)
            for i in range(1,m+1):
                lenHset[i-1].add(hs.query(0,i))
        ans = 0
        cur_r = 0 
        nxt_r =0
        hst = StringHash(target)

        for i in range(n):
            check = lambda sz: hst.query(i,i+sz+1) not in lenHset[sz]
            sz = bisect_left(range(min(n-i,mxl)),True,key=check)
            nxt_r = max(nxt_r , i+sz)
            if i ==cur_r:
                if i ==nxt_r:
                    return -1
                cur_r = nxt_r
                ans +=1
        return ans
        




re =Solution().minValidStrings(words = ["abc","aaaaa","bcdef"], target = "aabcdabc")
print(re)