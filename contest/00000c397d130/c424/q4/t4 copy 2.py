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
        
        
        
        def check(mid):
            rgls= []
            for a,b in ls[0]:
                if b-mid>a+mid:
                    return False
                rgls.append([b-mid,a+mid])
            for a,b in ls[1]:
                if b-a>3*mid:
                    return False
                rgls.append([a-mid,a+mid])
                rgls.append([b-mid,b+mid])
                #rgls.append([b-mid,a+mid])
            rgls.sort()
            cnt = 0
            lst=-10**30
            res =[]
            for a,b in rgls:
                if a >lst:
                    #print("ac",lst)
                    if lst>-10**30:
                        res.append(lst)
                    lst = b 
                    cnt +=1
                else:
                    lst = min(lst,b)
            res.append(lst)
            print(res,mid,rgls)
            # if mid ==4:
            #     print(res,rgls,mid,ls,"a",lst)
            #print(rgls)
            if len(res)<=2:
                if len(res) ==1:
                    for a,b in ls[1]:
                        if abs(a-res[0])> mid or abs(b-res[0]) >mid:
                            return False
                    return True
                #print(res)
                x1,x2 = res[0],res[1]
                for a,b in ls[1]:
                    if abs(a-x2) > mid and abs(b-x1) > mid and x2-x1 >mid:
                        return False
                for a,b in ls[0]:
                    if (abs(a-x1) > mid or abs(b-x1)>mid) and (abs(a-x2)>mid or abs(b-x2)>mid):
                        return False
                return True
            return False
            

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
            



        





re =Solution().minDifference([-1,483,-1,-1,202,-1,-1,478])
print(re,94)
# re =Solution().minDifference([-1,606,511,-1,-1,551,484,-1,349])
# print(re,95)
# re =Solution().minDifference([1,2,-1,10,8])
# print(re,4)
# re =Solution().minDifference([14,-1,-1,46])
# print(re,11)
# re =Solution().minDifference([238,475,-1,592,-1,512,-1,-1,31])
# print(re,237)
# re = Solution().minDifference([39,-1,40,-1,-1,46,-1,47])
# print(re,3)
# re = Solution().minDifference([-1,10,9,8,7,6,5,4,3,2,-1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,-1,19,20])
# print(re,4)
# re = Solution().minDifference([34,-1,40,-1,-1,46,-1,52])
# print(re,6)