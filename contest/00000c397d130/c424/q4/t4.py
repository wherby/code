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
        ls2 =[]
        for a,b in ls[0]:
            ls1.append(a)
            ls1.append(b)
        for a,b in ls[1]:
            ls2.append(a)
            ls2.append(b)
        ls1.sort()
        ls2.sort()
        ls3 =list(ls[0])
        ls4 =list(ls1)
        if len(ls2)>0:
            ls3.append([ls2[0],ls2[-1]])
            ls4.append(ls2[0])
            ls4.append(ls2[-1])
        ls4.sort()
        def check(mid):
            x,y = -1,-1
            #print(x,y,ls,mid)
            if len(ls2)>0:
                x= ls2[0]+mid
                y = ls2[-1] -mid
                if y> x +mid:
                    return False
                if y<=x:
                    y = x
                else:
                    y = x +mid
                for f,t in ls[1]:
                    if (abs(f-x) > mid or abs(t-y) > mid ) and (abs(x-f) > mid or abs(x-t)>mid) and (abs(y-f) > mid or abs(y-t)>mid):
                        #print(x,y,f,t)
                        return False 
            #print(x,y,"a")
            a = ls[0]
            t=ls1
            if y <=x:
                y =-1 
                x = -1
                a = ls3
                t= ls4
            #print(t,a)
            if len(a)>0:     
                if x ==-1 :
                    x = t[0]+mid 
                if y == -1:
                    y = t[-1] -mid 
            #print(x,y)
            #print(a)
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
        #print(check(237))
        #print(ls,check(95))
        return l
            



        





# re =Solution().minDifference([-1,483,-1,-1,202,-1,-1,478])
# print(re,94)
# re =Solution().minDifference([-1,606,511,-1,-1,551,484,-1,349])
# print(re,95)
# re =Solution().minDifference([1,2,-1,10,8])
# print(re,4)
# re =Solution().minDifference([14,-1,-1,46])
# print(re,11)
re =Solution().minDifference([238,475,-1,592,-1,512,-1,-1,31])
print(re,237)