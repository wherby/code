from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = s.split(" ")
        res =[]
        for t in ls:
            if not t[0].isalpha():
                res.append(t)
        #print(res)
        res = list(map(lambda x: int(x),res))
        n = len(res)
        iT=True
        for i in range(1,n):
            if res[i] <= res[i-1]:
                iT=False
        return iT
#s = "hello world 5 x 5"
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
re = Solution().areNumbersAscending(s)
print(re)