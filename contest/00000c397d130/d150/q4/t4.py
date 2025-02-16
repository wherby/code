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
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        ls = p.split("*")
        ls = list(filter(lambda a:len(a)>0,ls))
        if len(ls) == 0:
            return 0 
        sh = StringHash(s)
        lls = [[] for _ in range(len(ls))]
        n = len(s)
        for i,t1 in enumerate(ls):
            m = len(t1)
            s1 = StringHash(t1)
            k1 = s1.query(0,m)
            for j in range(n-m+1):
                if sh.query(j,j+m) == k1:
                    lls[i].append(j)
        ret = n +1
        for a in lls[0]:
            start = a 
            nx = a + len(ls[0])
            for j in range(1,len(ls)):
                k = bisect_left(lls[j],nx)
                if k >=len(lls[j]):
                    nx = 10**10 
                else:
                    nx = lls[j][k] + len(ls[j])
                #print(k,nx,start,"*",j)
            ret = min(ret,nx-start)
            #print(ret,nx,start)
        #print(lls)
        return ret if ret <= n else -1





#re =Solution().shortestMatchingSubstring(s = "baccbaadbc", p = "cc*baa*adb")
re =Solution().shortestMatchingSubstring(s = "baccbaadbc", p ="cc*baa*adb")
print(re)