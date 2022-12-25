from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter
from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0
        c2 =  defaultdict(int)
        for w in words:
            c = Counter([a for a in w])
            k = list(c.keys())
            k.sort()
            k = tuple(k)
            cnt += c2[tuple(k)]
            c2[k] +=1
        return cnt





re =Solution().similarPairs(["aba","aabb","abcd","bac","aabc"])
print(re)