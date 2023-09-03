from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        ls = []
        for i,a in enumerate(nums):
            if a %modulo ==k:
                ls.append(i)
        m = len(ls)
        kk = len(ls)//modulo
        acc = 0 
        ls = [-1]+ ls + [n]
        if k==0:
            #print(ls,n)
            for i in range(1,m+2):
                b  = ls[i]-ls[i-1]
                acc += b*(b-1)//2
                #print(acc)
            for i in range(1,kk+1):
                for j in range(i*modulo-1,m):
                    #print(j+2,j+1,j-i*modulo+2,j-i*modulo+1)
                    acc += (ls[j+2]-ls[j+1]) *(ls[j-i*modulo+2]-ls[j-i*modulo+1])
        else:
            #print(ls)
            for i in range(kk+1):
                for j in range(i*modulo-1 +k,m):
                    #print(i,j+2,j+1,j-i*modulo-k+2,j-i*modulo-k+1)
                    acc += (ls[j+2]-ls[j+1]) *(ls[j-i*modulo-k+2]-ls[j-i*modulo-k+1])
        return acc





re =Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)
print(re)