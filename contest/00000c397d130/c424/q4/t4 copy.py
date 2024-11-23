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
        
        ls[0].sort()
        ls[1].sort()
        ls1 =[]
        for a,b in ls[0]:
            ls1.append(a)
            ls1.append(b)
        ls1.sort()
        def check(mid):
            x,y = -1,-1
            a = ls[1]
            cur =-1
            if len(a) >0:
                cur=x = a[0][0] + mid

            for f,t in a:
                if abs(cur-f) > mid:
                    if y == -1:
                        cur = y= f + mid
                        if abs(cur - t) > mid:
                            # print(cur,x,y,"t",t)
                            return False
                    elif abs(x-f)> mid:
                        # print(x,y,cur,f,x)
                        # print(ls)
                        return False
                if abs(cur - t) > mid:
                    if y == -1:
                        cur = y = x + mid 
                        if abs(cur -t) >mid:
                            #print(cur,x,y,t)
                            return False 
            #print(x,y,ls,mid)
            a = ls[0]
            if len(a)>0:     
                if x ==-1 :
                    x = ls1[0]+mid 
                if y == -1:
                    y = ls1[-1] -mid 
            
            for f,t in a:
                if (abs(f-x) > mid or abs(t-x) > mid ) and (abs(y-f) > mid or abs(y-t)>mid):
                    return False        
            return True
        l ,r = mx,10**10
        while l<r:
            mid =(l+r)>>1
            #print(mid,check(mid))
            if check(mid):
                r = mid 
            else:
                l =mid +1
        #print(check(137))
        return l
            



        





re =Solution().minDifference([-1,483,-1,-1,202,-1,-1,478])
print(re,94)
re =Solution().minDifference([-1,606,511,-1,-1,551,484,-1,349])
print(re,95)