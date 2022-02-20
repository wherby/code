from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        def check(a):
            cnt =0 
            while a >0:
                cnt += a%10
                a = a //10
            return cnt %2 ==0
        sm = 0
        for i in range(1,num+1):
            if check(i):
                sm +=1
                #print(i)
        return sm

re = Solution().countEven(30)
print(re)