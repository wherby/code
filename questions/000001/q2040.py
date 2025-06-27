FILEDEBUG =False
if FILEDEBUG:
    import os

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/outt4.fist.txt', 'w')
    sys.stdout = f
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l1,l2 = [],[]
        for a in nums1:
            if a >=0:
                l1.append(a)
            else:
                l2.append(a)
        l, r = -10**20,10**20
        n= len(nums1)
        m = len(l2)
        m2 = len(l1)
        def verify(md):
            cnt = 0
            for a in nums2:
                if a ==0:
                    if md >=0:
                        cnt += n 
                elif a >0 and md >=0:
                    #print(cnt)
                    t = md//a 
                    cnt+= bisect_right(l1,t)+m
                    #print(cnt,a,md,l1,bisect_right(l1,t),m)
                elif a > 0 and md <0:
                    t = md //a 
                    cnt += bisect_right(l2,t)
                    #print(cnt,a,t)
                elif a <0 and md >0:
                    t = md /a 
                    cnt += m- bisect_left(l2,t)+m2
                    #print(cnt,m,t,bisect_left(l2,t),l2)
                elif a <0 and md <=0 :
                    t = md /a 
                    cnt += m2 - bisect_left(l1,t)
                    #print(cnt,a,t,"a",l1,bisect_right(l1,t))
            #print(cnt,md)
            return cnt >= k
        while l <r :
            md = (l+r)>>1
            if verify(md):
                r = md 
            else:
                l = md +1
        return l

re = Solution().kthSmallestProduct(nums1 = [-9,6,10], nums2 = [-7,-1,1,2,3,4,4,6,9,10], k = 15)
print(re)