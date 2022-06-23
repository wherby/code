from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def fn(ls):
            if len(ls) ==1:
                return ls[0]
            tls = []
            flip =0
            for i in range(0,len(ls),2):
                if flip %2 ==0:
                    tls.append(min(ls[i],ls[i+1]))
                else:
                    tls.append(max(ls[i],ls[i+1]))
                flip +=1
            return fn(tls)
            
        return fn(nums)

re = Solution().minMaxGame( [70,38,21,22])
print(re)