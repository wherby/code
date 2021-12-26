from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        if len(sentences) ==0:
            return 0
        ls = list(map(lambda x: x.split(" "),sentences))
        nums = map(lambda x: len(x),ls)
        return max(nums)