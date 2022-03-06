from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


from collections import defaultdict
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        dic = defaultdict(int)
        n = len(nums)
        for i in range(n-1):
            if nums[i] == key:
                dic[nums[i+1]] +=1
        mx =0
        re =-1
        for key,v in dic.items():
            if v > mx:
                mx = v
                re  = key
        return re