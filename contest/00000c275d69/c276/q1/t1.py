from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        n= len(s)
        d = k-n%k if n%k !=0 else 0
        s = s + fill*d
        n = len(s)
        re= []
        for i in range(0,n,k):
            re.append(s[i:i+k])
        return re