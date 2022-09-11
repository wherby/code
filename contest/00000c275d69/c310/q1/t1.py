from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        mx =0
        ret =-1
        for i in sorted(dic.keys()):
            if dic[i]> mx and i%2==0:
                mx = dic[i]
                ret = i 
        return ret





re =Solution().mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290])
print(re)