from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def temperatureTrend(self, temperatureA, temperatureB):
        """
        :type temperatureA: List[int]
        :type temperatureB: List[int]
        :rtype: int
        """
        n = len(temperatureA)
        
        def getArr(ls):
            ret = []
            for i in range(1,n):
                if ls[i]> ls[i-1]:
                    ret.append(1)
                elif ls[i]<ls[i-1]:
                    ret.append(-1)
                else:
                    ret.append(0)
            return ret
        lsa,lsb = getArr(temperatureA),getArr(temperatureB)
        mx =0
        acc =0 
        for i in range(n-1):
            if lsa[i] ==lsb[i]:
                acc +=1
                mx =max(mx,acc)
            else:
                acc =0 
        return mx



re =Solution().temperatureTrend([1,-15,3,14,-1,4,35,36],[-15,32,20,9,33,4,-1,-5])
print(re)
