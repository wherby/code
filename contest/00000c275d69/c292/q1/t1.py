from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n =len(num)
        res =[num[i:i+3] for i in range(n-2)]
        res = sorted(res,key = lambda x: int(x))
        res = list(filter(lambda x :x[0]==x[1]==x[2],res))
        if len(res)==0:
            return "" 
        return list(res)[-1]
        
re = Solution().largestGoodInteger("6771339")
print(re)