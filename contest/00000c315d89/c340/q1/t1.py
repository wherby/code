from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue

def get_prime(n):
    visited=[0]*(n+2)
    res =[]
    for i in range(2,n+1):
        if visited[i]: continue
        res.append(i)
        for j in range(i,n+1,i):
            visited[j] =1
    return res

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ret = 0
        n= len(nums)
        mx = 0
        for ls in nums:
            for a in ls:
                mx = max(mx,a)
        pls = get_prime(mx)
        pls =set(pls)
        for i in range(n):
            if nums[i][i] in pls:
                ret = max(ret,nums[i][i])
            if nums[i][n-1-i] in pls:
                ret = max(ret,nums[i][n-1-i])
        return ret
            





re =Solution().diagonalPrime( [[1,2,3],[5,6,7],[9,10,11]])
print(re)