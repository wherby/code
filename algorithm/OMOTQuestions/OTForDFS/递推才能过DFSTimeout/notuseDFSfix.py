# https://leetcode.cn/contest/weekly-contest-419/problems/count-the-number-of-winning-sequences/submissions/572285010/

from typing import List, Tuple, Optional
import sys
sys.setrecursionlimit(1500000)

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
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9+7
        n = len(s)
        dic = {"F":0,"W":1,"E":2}
        acc =0
        pd ={}
        for a in "FWE":
            if  a == s[0]:
                pd[(a,0)] =1
            elif ((dic[a] +3)-dic[s[0]])%3 ==1:
                pd[(a,1)] =1
            else:
                pd[(a,-1)] =1 
        for aa in s[1:]:
            tmp = defaultdict(int)
            for (a,i1),c1 in pd.items():
                c1 = c1%mod
                for b in "FWE":
                    if a ==b:continue
                    if b ==aa :
                        tmp[(b,i1)] += c1
                    elif ((dic[b] +3)-dic[aa])%3 ==1:
                        tmp[(b,i1+1)] +=c1
                    else:
                        tmp[(b,i1-1)] +=c1 
            pd = tmp
        for  (a,i1),c1 in pd.items():
            if i1 >0:
                acc += c1 
        return acc %mod






re =Solution().countWinningSequences("FWEFW"*200)
print(re)