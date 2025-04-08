#  OT
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

from itertools import pairwise
class SL:
    def __init__(self,n):
        self.sl=[-1]
        for i in range(n):
            self.sl.append(i)
        self.sl.append(n)

    def remove(self,i):
        self.sl.remove(i)
    
    def next(self,i):
        k =bisect_left(self.sl,i)
        return self.sl[k+1]
    
    def pre(self,i):
        k = bisect_left(self.sl,i)
        return self.sl[k-1]

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0
        ls = SortedList()
        n = len(nums)
        sl = SL(n)
        for i in range(n-1):
            ls.add((nums[i]+nums[i+1],i,i+2))
        isG = False 
        cnt =0
        rm = {}
        while isG ==False and len(ls):
            while len(ls) and ls[0][1] != 0:
                a,b,c = ls[0]
                ls.remove((a,b,c))
                #print(sl.sl,b,"a")
                if b in rm or sl.next(b) ==n or   sl.next(sl.next(b)) != c:
                    continue
                nums[b] =a 
                cnt +=1
                rm[sl.next(b)] =1
                sl.remove(sl.next(b))
                #print(sl.sl,b)
                if sl.next(b) != n :
                    ls.add((nums[b] + nums[sl.next(b)],b,sl.next(sl.next(b))))
                if sl.pre(b) != -1:
                    ls.add((nums[sl.pre(b)] + nums[b],sl.pre(b),sl.next(b)))
            if len(ls):
                t = ls[0]
            else:
                break
            while len(ls) and( t[1] in rm or  sl.next(t[1]) == n or sl.next(sl.next(t[1])) != t[2]):
                ls.remove(t)
                if len(ls):
                    t = ls[0]
                else:
                    break
                    
            #print("a")
            isG = True 
            for a,b in pairwise(sl.sl[1:-1]):
                if nums[a] >nums[b]:
                    isG = False
                    break
            if isG == False:
                a,b,c =ls[0]
                #print(a,b,c,rm,sl.sl,sl.next(sl.next(b)),c)
                ls.remove((a,b,c))
                nums[b] =a 
                cnt +=1
                rm[sl.next(b)]=1
                sl.remove(sl.next(b))
                if sl.next(b) != n :
                    ls.add((nums[b] + nums[sl.next(b)],b,sl.next(sl.next(b))))
                if sl.pre(b) != -1:
                    ls.add((nums[sl.pre(b)] + nums[b],sl.pre(b),sl.next(b)))
                # t = ls[0]
                # while t[1] in rm or sl.next(t[1]) ==n or sl.next(sl.next(t[1])) != t[2]:
                #     ls.remove(t)
                #     t = ls[0]
        #print(sl.sl,ls,nums)
        return cnt


re =Solution().minimumPairRemoval([-7,-2,-4,4,8,-6,0,0,4,5,1,-8])
print(re)