# common include
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        ls = [0]*100
        def getNum(x):
            cnt =0
            while x >0:
                cnt += x%10
                x= x//10
            return cnt
        for i in range(lowLimit,highLimit+1):
            t = getNum(i)
            ls[t] +=1
        mx =0
        for i in ls:
            mx = max(mx,i)
        return mx