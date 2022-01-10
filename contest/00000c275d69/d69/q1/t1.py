from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        ls = title.split(" ")
        for i in range(len(ls)):
            t = ls[i]
            if len(t)<=2:
                t= t.lower()
            else:
                t = t.capitalize()
            ls[i] = t
        return " ".join(ls)

re =Solution().capitalizeTitle("i lOve leetcode")
print(re)