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
    def minimumDifference(self, nums: List[int], kk: int) -> int:
        ls= [deque([]) for _ in range(32)]
        for i,a in enumerate(nums):
            for j in range(32):
                if (1<<j)&a==0:
                    ls[j].append(i)
        mx =10**20
        
        for i in range(len(nums)):
            for j in range(32):
                while len(ls[j]) and ls[j][0] < i:
                    ls[j].popleft()
            dic = defaultdict(list)
            for j in range(32):
                if len(ls[j]):
                    dic[ls[j][0]].append(j)
            ks =list(dic.keys())
            ks.sort()
            acc =nums[i]
            #print(dic,acc)
            mx = min(mx,abs(acc-kk))
            for k in ks:
                for j in dic[k]:
                    if ((1<<j)&acc):
                        acc -= 1<<j
                mx = min(mx,abs(acc-kk))
                #print(acc,kk,i,k,mx)
        return mx





re =Solution().minimumDifference(nums = [3,1,81,17,14], kk = 57)
#print(re)


def f(a:int):
    def lens(str:str)->int:
        return a*len(str)
    return lens

def r(a:int)->str:
    return "a"*a

c = f(2)
print(c("nn"))
print(r(2))

def fx(a):
    return f(a)(r(a))

print(fx(4))