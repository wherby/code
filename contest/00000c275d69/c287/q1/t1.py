from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        c1,c2 = int(current[:2]),int(current[3:])
        c3,c4 =int(correct[:2]),int(correct[3:])
        a1 = c1*60 + c2
        b1  = c3 *60 + c4
        res = b1 -a1
        cnt = 0
        ls = [60,15,5,1]
        for a in ls:
            cnt += res //a 
            res = res %a 
        return cnt


re = Solution().convertTime(current = "02:30", correct = "04:35")
print(re)