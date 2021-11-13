from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
import collections

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dic = defaultdict(int)
        for a in word1:
            dic[a] +=1
        for a in word2:
            dic[a] -=1
        for k,v in dic.items():
            if abs(v)>3:
                return False
        return True
        

re =Solution().checkAlmostEquivalent(word1 = "cccddabba", word2 = "babababab")
print(re)