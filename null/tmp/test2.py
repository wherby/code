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

import math
#    5
#  2  3
#    11,12
# 3.       4

def sert(n):
    if n < 0:
        return -1
    l,r = 0, n 
    while l + 0.00001 <r :
        mid =(l+r)/2 
        if mid *mid <= n:
            l = mid 
        else:
            r = mid 
    n,n1 = int(l),int(l) +1
    return n if l-n < n1-l else n1

for  i in range(-1,19):
    print(sert(i),i)

ls = [0,10**20,72,73]
for a in ls:
    print(a, sert(a),math.sqrt(a))

    
