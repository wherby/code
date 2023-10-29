from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9+7
        acc = 0
        dic ={}
        sm = 0
        n = len(nums)
        sm1 =0
        # for i in range(4):
        #     sm1 += (i+1)*(i+1)*(4-i)
        # print(sm1)
        for i in range(1,n+1):
            sm += i**2 *(n+1-i)
            sm %= mod
        nc = 0
        print(sm)
        for i,a in enumerate(nums):
            if a not in dic:
                dic[a] =i
            else:
                nc+=1
                print(i,i-nc+i-nc+3,n-nc+n-nc+1,n-i,(i-nc+i-nc+3 + n-nc+n-nc+1)//2*(n-i),nc)
                sm -= (i-nc+i-nc+3 + n-nc+n-nc+1)//2*(n-i)
                sm %=mod 
        return sm
                



re =Solution().sumCounts( [2,2,5,5])
print(re)