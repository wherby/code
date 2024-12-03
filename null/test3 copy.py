from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from sortedcontainers import SortedDict,SortedList
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def bs(ls,t):
            n = len(ls)
            l,r = 0, n-1
            
            while l < r:
                mid = (l+r)>>1
                if ls[mid] ==t:
                    return True
                elif ls[mid]< t:
                    l = mid +1
                else:
                    r = mid-1
            return ls[l] == t

        def query(ls,t):
            if ls[0] <= ls[-1]:
                return  bs(ls,t)
            else:
                return find1(ls,t)

        def find1(ls,t):
            
            if len(ls) == 1:
                if ls[0] != t:
                    return False
                return True
            n = len(ls)
            mid = n //2 
            lst,rst = ls[:mid],ls[mid:]
            return query(lst,t) or query(rst,t)

        def find(ls,t):
            while ls[-1] == ls[0] and len(ls) >1:
                ls.pop()
            return  find1(ls,t)
        return find(nums,target)

ls = [6,8,9,11,12,12,12,1,3,5,6]
#
#ls = [ 6,,8,9,11,12],[12,12,12,12,12]


# L,  R
# [6,6,6,6,1,2,3,5] 
#
# target =15
# print(find(ls,10))
s =Solution()
# for i in range(20):
#     print((s.search(ls,i)) , i in ls,i)
print(s.search([1],1))