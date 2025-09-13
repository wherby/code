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
    def bowlSubarrays(self, nums: List[int]) -> int:
        cnt = 0 
        st= []
        sl = SortedList()
        for i,a in enumerate(nums):
            while st and a > nums[st[-1]]:
                if i - st[-1]>1:
                    cnt +=1
                #print(cnt,st[-1],i,"a")
                sl.remove(nums[st[-1]])
                st.pop()
            k = sl.bisect_right(a)
            #print(k,a,len(sl),sl,st)
            if k +1 <= len(sl):
                k +=1 
            cnt += k
            
            if k>0 and st[-1] +1 ==i:
                cnt -=1
                #print(st,k,i,cnt)
            st.append(i)
            sl.add(a)
            #print(i,cnt)
        return cnt





re =Solution().bowlSubarrays([2,5,3,1,4])
print(re)