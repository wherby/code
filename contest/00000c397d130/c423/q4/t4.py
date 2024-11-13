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
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        mod = 10**9+7
        n = len(s)
        acc =0
        for i in range(1,n):
            for j in range(k):
                if i<j:continue
                acc += math.comb(i-1,j)
                #print(i,j,math.comb(i-1,j))
        
        @cache
        def getC(n,m):
            if n ==0:
                return 1
            if m<0:
                return 0
            if m ==0:
                return 1
            acc = 0

            for j in range(m+1):
                if n < j: continue
                acc += math.comb(n,j)
                #print(i,j,math.comb(i,j),n,m)
            return acc
        print(acc)
        @cache
        def dfs(i,res,equal):
            if res<0:
                return 0
            if i== n:
                return 0
            ret =0
            if s[i] =="1":
                ret += getC(n-i-1,res)
                #print(n-i-1,res,getC(n-i-1,res),ret)
                if res>=0:
                    ret += dfs(i+1,res-1,True)
                    #print(ret,"a",dfs(i+1,res-1,True),i+1,res-1)
            else:
                ret += dfs(i+1,res,True)

            return ret
        acc += dfs(1,k-1,True)
        #print(dfs(1,k-1,True))
        return acc %mod





#re =Solution().countKReducibleNumbers(s = "111", k = 1)
#re =Solution().countKReducibleNumbers(s = "1000", k = 2)
# re =Solution().countKReducibleNumbers(s = "11", k = 2)
# print(re,2)
# re =Solution().countKReducibleNumbers(s = "1101", k = 5)
# print(re,12)
# print(re)
re =Solution().countKReducibleNumbers(s = "10010", k = 2)
print(re)

for i in range(18):
    if bin(i).count("1")>0 and bin(i).count("1")<=2:
        print(i,bin(i))