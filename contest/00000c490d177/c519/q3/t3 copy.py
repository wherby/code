# https://leetcode.cn/problems/count-shadow-pairs-i/description/
# 使用替代方式
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
    def shadowPairs(self, nums: list[int]) -> int:
        sl = SortedList([])
        que=[]
        cnt =0 
        c= defaultdict(int)
        for a in nums:
            while que and a < que[-1]:
                b = que[-1]
                que.pop()
                c[b] -=1
            k =len(que) -c[a]
            cnt += k
           # print(cnt,k,sl,a,que)
            que.append(a)
            c[a]+=1
            
        return cnt





re =Solution().shadowPairs([6,7,6,6,7])
print(re)