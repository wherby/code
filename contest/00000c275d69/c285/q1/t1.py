from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        state =0
        NewState = 0
        n = len(nums)
        cnt = 0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                NewState = 1
            elif nums[i] < nums[i-1]:
                NewState = -1
            else:
                NewState = state
            if state != 0 and state != NewState:
                cnt +=1
            #print(i,nums[i],cnt)
            state = NewState
        return cnt

re = Solution().countHillValley([49,16,11,24,82,24,73,61,62,44,25,59,3,57,62,7,38,61,22,92,90,60,28,21,37,54,43,14,3,64,48,51,55,55,58,43,67,46,36,32,78])
print(re)