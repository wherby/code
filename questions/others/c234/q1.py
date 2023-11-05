# common include
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter


class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        ls=[]
        t =""
        for i in word:
            if i.isalpha():
                if t !="":
                    ls.append(t)
                t =""
            else:
                t = t+i
        if t!="":
            ls.append(t)
        ls = map(lambda x: int(x),ls)
        d ={}
        for i in ls:
            d[i]= 1
        return len(d.keys())

re =Solution().numDifferentIntegers("a123bc34d8ef34")