# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/description/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        dic = {}
        items.sort(reverse= True)
        sm = 0
        cand = []
        for i in range(k):
            a,b = items[i]
            if b not in dic:
                dic[b] =1
            else:
                cand.append(a)
            sm += a 
        cand.sort(reverse= True)
        ss = len(dic.items())
        sm += ss*ss
        #print(sm,ss)
        acc =sm
        for a,b in items[k:]:
            if b not in dic and cand :  ## 要达到最多K种type，一定是第一次遇到的最大的那个type的值被使用
                acc+= ss+ss+1+a - cand[-1]
                cand.pop()
                dic[b] =1
                ss +=1
                sm = max(sm,acc)
        return sm
        





re =Solution().findMaximumElegance([[2,2],[8,6],[10,6],[2,4],[9,5],[4,5]],4)
print(re)