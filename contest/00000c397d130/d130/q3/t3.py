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

def getPre(s):
    pre = [[0 for _ in range(26)]]
    for a in s:
        pre.append(list(pre[-1]))
        pre[-1][ord(a)- ord('a')] +=1
    return pre

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        dic = {}
        pre = getPre(s)
        n = len(s)
        def isGood(i,j):
            tp = [(a-b) for a,b in zip(pre[i],pre[j])]
            tp =[a for a in tp if a != 0 ]
            #print(tp)
            return len(set(tp)) ==1 
        dic[0] =0
        for i in range(1,n+1):
            mx = i 
            for j in range(i):
                if isGood(i,j):
                    mx = min(mx,dic[j]+1)
                    #print(i,j)
                    #break
            dic[i] = mx
        #print(dic)
        #print(isGood(7,6))
        #print(isGood(4,0))
        return dic[n]
        





re =Solution().minimumSubstringsInPartition("bccbaacabc")
print(re)