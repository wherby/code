from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n  = len(nums)
        ls = []
        for i,a in enumerate(nums):
            ls.append((a,i))
        ls.sort()
        left =0
        leftValue = ls[0][0]
        st = SortedList([])
        for j in range(n):
            a,i = ls[j]
            while left<=j and   a - leftValue >=valueDifference:
                st.add(ls[left][1])
                left +=1
                if left < n:
                    leftValue=ls[left][0]
            if len(st) >0:
                if abs(i -st[0]) >=indexDifference:
                    return[st[0],i]
                if abs(i- st[-1])>= indexDifference:
                    return [st[-1],i]
            #print(st,left,j)
        return [-1,-1]
            





re =Solution().findIndices(nums = [5], indexDifference = 0, valueDifference = 0)
print(re)