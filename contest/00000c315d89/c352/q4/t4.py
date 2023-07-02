from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        acc = 0
        for i in range(n):
            cnt = 0
            sl = SortedList()
            kn = 0
            dic={}
            for j in range(i,n):
                a = nums[j]
                if a not in dic:
                    dic[a] =1
                    kn +=1
                    sl.add(a)
                    k = sl.index(a)
                    if kn>1:
                        cnt +=1
                    if k>0 :
                        if a -sl[k-1] ==1:
                            cnt -=1
                    if k< kn-1:
                        if sl[k+1] -a ==1:
                            cnt -=1
                    acc += cnt 
                    #print(cnt,sl,i)
                else:
                    acc +=cnt
        return acc
                    



re =Solution().sumImbalanceNumbers([1,3,3,3,5])
print(re)