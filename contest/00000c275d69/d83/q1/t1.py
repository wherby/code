from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        ls =[0]*14
        dic =defaultdict(int)
        for a in ranks:
            ls[a]+=1
        for s in suits:
            dic[s] +=1
        for k,v in dic.items():
            if v ==5:
                return "Flush"
        mx = 1 
        for i in range(14):
            mx =max(mx,ls[i])
        if mx >=3:
            return "Three of a Kind"
        if mx == 2:
            return "Pair"
        return "High Card"




re =Solution().bestHand(ranks = [13,13,13,13,3], suits = ["d","a","a","a","a"])
print(re)