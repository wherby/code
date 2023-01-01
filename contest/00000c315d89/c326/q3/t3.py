from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
from itertools import pairwise
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        ret = -1
        cnt =0 
        m = len(str(k))
        st =[]
        for a in s:
            st.append(a)
            if int(a)>k:
                return -1
            if int("".join(st))>k:
                
                cnt +=1
                st=[]
                st.append(a)
        if len(st)>0:
            cnt +=1
        return cnt
                            






re =Solution().minimumPartition(s = "65643379991964372", k = 5)
print(re)