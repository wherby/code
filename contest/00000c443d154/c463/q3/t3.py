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
    def minArraySum(self, nums: List[int], k: int) -> int:
        ls = []
        for a in nums:
            if a %k != 0:
                ls.append(a)
        visit ={}
        visit[0] = 0
        acc = 0
        st = []
        print(ls)
        for a in ls:
            acc +=a 
            acc =acc%k 
            #print(acc,st,a)
            if acc in visit:
                t =visit[acc]
                acc =(acc-a)%k
                while len(st) > t :
                    #print(acc,st)
                    del visit[acc]
                    t1 =st.pop()
                    acc = (acc -t1)%k
                    
            else:
                st.append(a)
                visit[acc] = len(st)
            print(visit,st,acc)
        return sum(st)




#re =Solution().minArraySum(nums = [71,91,43,49,80,93,65], k = 205)
re = Solution().minArraySum([58,68,57,71,52,6,40,22,13,29,26,17,47,31,51,73,59,69,37,14],34)
print(re)