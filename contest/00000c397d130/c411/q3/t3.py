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

import sys
sys.set_int_max_str_digits(100000)

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        hf = (n+1)//2
        if k %2==0:
            start = 10**hf -10**hf//10
        else:
            start = 10**hf -1
        if k%5 ==0:
            start = 10**hf-10**hf//10*4
        if k%4==0:
            start = 10**hf -10**hf//100*11
        if k%8==0:
            start = 10**hf -10**hf//1000*111
        def verify(num):
            acc =0
            for a in num:
                acc = acc*10 + int(a)
                acc = acc%k 
            return acc ==0
        for i in range(start,-1,-1):
            if n %2 ==0:
                anh = str(i)[::-1]
            else:
                anh = str(i)[:-1][::-1]
            num= str(i) + str(anh)
            if verify(num):
                return num






re =Solution().largestPalindrome(13,8)
print(re)