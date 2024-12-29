# https://leetcode.cn/contest/weekly-contest-430/problems/find-the-lexicographically-largest-string-from-the-box-i/description/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends ==1:
            return word
        n = len(word)
        tlen = n-numFriends+1
        ans =""
        for i in range(n):
            l = min(tlen,n-i)
            ans = max(ans, word[i:i+l])
        return ans
    
        



re =Solution().answerString(word = "dbca", numFriends = 2)
print(re)