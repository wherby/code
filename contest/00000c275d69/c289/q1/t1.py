from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def getNew(str1):
            n = len(str1)
            re=[]
            for i in range(0,n,k):
                re.append(str1[i:i+k])
            re = [str(sum(list(map(lambda y:int(y),x))))  for x in re]
            return re
        while len(s)>k:    
            res = getNew(s)
            s = "".join(res)
        return s
re = Solution().digitSum(s = "00000000", k = 3)
print(re)