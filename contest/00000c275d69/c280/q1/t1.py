from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        cnt = 0
        while num1*num2 >0:
            num1,num2= max(num1,num2),min(num1,num2)
            num1 = num1 -num2
            cnt +=1
            #print(num1,num2)
        return cnt

re = Solution().countOperations(2,3)
print(re)