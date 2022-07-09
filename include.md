# common include
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter
from functools import lru_cache
from functools import cache
##  @functools.lru_cache(None) 

from math import comb // use to combination

from sortedcontainers import SortedDict,SortedList
self.ls =SortedList()


#

from math import inf

# deque  https://www.geeksforgeeks.org/stack-in-python/   广度优先如果要效率可以使用
from collections import deque
 
stack = deque()

# format 
return [f"{j}/{i}" for i in range(2, n + 1) for j in range(1, i) if gcd(i, j) == 1]