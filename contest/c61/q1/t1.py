from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue

import math
class Solution:
    def countKDifference(self, nums, k) :
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                if  abs(nums[i] - nums[j]) == k:
                    cnt +=1
        return cnt 

print(Solution().countKDifference([1,2,2,1],1))