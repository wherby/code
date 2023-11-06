from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        n = len(rings)
        ls=[0]*(100+1)
        cor=0
        for i,c in enumerate(rings):
            if i%2==0:
                if c =="R":
                    cor =1
                elif c =="G":
                    cor =2
                else:
                    cor =4
            else:
                idx = int(c)
                ls[idx] = ls[idx] | cor
        cnt =0
        for i in range(10):
            if ls[i] == 7:
                cnt +=1
        return cnt

re = Solution().countPoints(rings = "B0R0G0R9R0B0G0")
print(re)

