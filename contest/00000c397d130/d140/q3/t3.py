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
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m = len(word1)
        n = len(word2)
        dp1= [0]*(m+1) 
        dp2 = [0]*(m+1) 
        idx =0
        for i,a in enumerate(word1):
            if idx <n and a ==word2[idx]:
                idx+=1
            dp1[i+1]= idx
        wd2r = word2[::-1]
        idx = 0
        for i,a in enumerate(word1[::-1]):
            if idx<n and a == wd2r[idx]:
                idx +=1
            dp2[i+1] = idx
        ret = []
        # if dp1[-1] ==n:
        #     idx = 0
        #     for i, a in enumerate(word1):
        #         if idx<n and a ==word2[idx]:
        #             ret.append(i)
        #             idx +=1
        #     pre = -1
        #     print("a",ret)
        #     for i,a in enumerate(ret):
        #         if a != pre+1 :
        #             ret[i]=pre+1
        #             return ret
        #         pre = a 
        #     return ret
        # else:
        #print(dp1,dp2)
        for i in range(0,m):
            if i<n-1 and word1[i] == word2[i]:continue
            #print(i, dp1[i]+dp2[(m-i)], dp1[i], dp2[(m-i)])
            if dp1[i]+dp2[(m-i-1)] >= n-1:
                #print("c")
                ret =[]
                idx = 0
                for j,a in enumerate(word1[:i]):
                    if a == word2[idx]:
                        ret.append(j)
                        idx +=1
                #print(ret,i)
                if len(ret) ==0:
                    ret.append(0)
                else:
                    ret.append(ret[-1]+1)
                idx+=1
                for j,a in enumerate(word1[i+1:],i+1):
                    if idx<n and a == word2[idx]:
                        ret.append(j)
                        idx+=1
                return ret 
        
        return ret


#re =Solution().validSequence(word1 = "eeddeeeeee", word2 ="dd" )
#re =Solution().validSequence(word1 = "bacdc", word2 = "abc" )
#re =Solution().validSequence("ghhgghhhhhh", word2 ="gg" )
re =Solution().validSequence("daeebdfaeffeneeeeabcbcdf", word2 ="effefeee" )
print(re)