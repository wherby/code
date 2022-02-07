from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ls1,ls2=[],[]
        for i in range(n):
            if i %2 ==0:
                ls1.append(nums[i])
            else:
                ls2.append(nums[i])
        ls1 = sorted(ls1)
        ls2 = sorted(ls2,reverse=True)
        ls=[]
        for i in range(n):
            if i%2 ==0:
                ls.append(ls1[i//2])
            else:
                ls.append(ls2[i//2])
        return ls

re  =Solution().sortEvenOdd([4,1,2,3])
print(re)