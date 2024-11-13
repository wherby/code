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
        dic = defaultdict(list)
        for i in range(1,801):
            cnt = 0
            cur =i 
            while cur != 1:
                cur = bin(cur).count("1")
                cnt +=1
            dic[cnt].append(i)
        cands = []
        for i in range(k):
            cands.extend(dic[i])
        n = len(s)
        acc =0 
        for a in cands:
            if a >=n-1: continue
            for j in range(1,n):
                if a>j:continue
                acc += math.comb(j-1,a-1)
                print(a-1,j-1,math.comb(j-1,a-1))
        cands.sort()
        print(acc,cands[:10],n-1)
        @cache
        def getC(n,m):
            if n ==0:
                return 0
            if m<0:
                return 0
            if m>n:
                return 0

            return math.comb(n,m)
        @cache
        def dfs(i,res,equal):
            if n-i-1 < res:
                return 0
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
        #print(cands)
        for a in cands:
            if a > n : continue
            acc +=dfs(1,a-1,True)
            #print(a,n,dfs(1,a-1,True))
        return acc




#re =Solution().countKReducibleNumbers(s = "111", k = 1)
#re =Solution().countKReducibleNumbers(s = "1000", k = 2)
# re =Solution().countKReducibleNumbers(s = "11", k = 2)
# print(re,2)
re =Solution().countKReducibleNumbers(s = "1101", k = 5)
print(re,12)
# print(re)
#re =Solution().countKReducibleNumbers(s = "10010", k = 2)
print(re)

# for i in range(18):
#     if bin(i).count("1")>0 and bin(i).count("1")<=2:
#         print(i,bin(i))