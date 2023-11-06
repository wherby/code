from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
import itertools

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        lss = itertools.combinations(digits,3)
        dic={}
        for ls in lss:
            re =itertools.permutations(ls)
            for a in re:
                if a [0] ==0 or a[2]%2 ==1: continue
                t = a[0]*100 + a[1]*10 +a[2]
                dic [t] =1
        res=list(dic.keys())
        res.sort()
        return res

re =Solution().findEvenNumbers(digits = [0,2,0,0])
print(re)
