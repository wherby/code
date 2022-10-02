from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache
from typing import Counter

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n= len(word)
        for i in range(n):
            ls = word[:i] + word[i+1:]
            c = Counter(ls)
            m = len(c.keys())
            d = (n-1) //m
            isGood =True
            for k,v in c.items():
                if v != d:
                    isGood = False
            if isGood:
                return True
        return False





re =Solution().equalFrequency("abcc")
print(re)