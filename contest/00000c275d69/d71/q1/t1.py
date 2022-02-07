from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        ls = sorted(list(map(lambda x:int(x),num)))
        a1,a2 = int(ls[0]*10+ls[3]) ,int(ls[1]*10+ls[2])
        return a1+a2
        

re =Solution().minimumSum(2932)
print(re)