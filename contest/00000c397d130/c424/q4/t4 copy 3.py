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

from sortedcontainers import SortedDict,SortedList

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        mx =0
        state =0
        lst = -1
        ls=[[],[]]
        for a in nums:
            if a != -1:
                if lst == -1:
                    lst = a 
                    if state >0:
                        ls[0].append([a,a])
                        state =0
                else:
                    if state == 0:
                        mx = max(mx,abs(a - lst))
                        lst = a 
                    elif state == 1:
                        t = [lst,a]
                        t.sort()
                        ls[0].append(t)
                        lst =a 
                        state = 0 
                    else:
                        t = [lst,a]
                        t.sort()
                        ls[1].append(t)
                        lst = a
                        state = 0
            else:
                if lst ==-1:
                    state =1
                else:
                    state +=1
        if state >0:
            ls[0].append([lst,lst])
        
        als = []

        
        for a, b in ls[0]:
            als.append(a)
            als.append(b)
        for a,b in ls[1]:
            als.append(a)
            als.append(b)
        als.sort()
        if len(als) ==0:
            return mx
        A,B = als[0], als[-1]
        for a, b in ls[0]:
            mx = max(mx,(min(B-a,b-A)+1)//2)
            #print(a,b,mx)
        #print(A,B,mx,als)
        for a, b in ls[1]:
            t= (B-A+2)//3
            mx = max(mx,min((min(B-a,b-A)+1)//2,t))
        return mx


        





# re =Solution().minDifference([-1,483,-1,-1,202,-1,-1,478])
# print(re,94)
# re =Solution().minDifference([-1,606,511,-1,-1,551,484,-1,349])
# print(re,95)
re =Solution().minDifference([1,2,-1,10,8])
print(re,4)
re =Solution().minDifference([14,-1,-1,46])
print(re,11)
re =Solution().minDifference([238,475,-1,592,-1,512,-1,-1,31])
print(re,237)
re = Solution().minDifference([39,-1,40,-1,-1,46,-1,47])
print(re,3)
re = Solution().minDifference([-1,10,9,8,7,6,5,4,3,2,-1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,-1,19,20])
print(re,4)
re = Solution().minDifference([34,-1,40,-1,-1,46,-1,52])
print(re,6)