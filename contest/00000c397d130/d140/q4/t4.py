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

def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] + i <= R:
                Z[i] = Z[k]
            else:
                L = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
        #print(i,L,R,Z)
    return Z

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
    def minStartingIndex(self, s: str, pattern: str) -> int:
        m = len(s)
        n = len(pattern)
        hs2 = StringHash(pattern)
        hs1 = StringHash(s)
        str= pattern+"#" + s 
        zarr = calculate_z_array(str)
        ls = zarr[n+1:]
        for i in range(m-n+1):
            t = ls[i] 
            #@print(hs2.query(t+1,n),hs1.query(i+t+1,i+n),t)
            if t+1>n or hs2.query(t+1,n)== hs1.query(i+t+1,i+n):
                return i 
        return -1





re =Solution().minStartingIndex(s = "dde", pattern = "d")
print(re)