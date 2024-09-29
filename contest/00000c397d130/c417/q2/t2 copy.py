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
from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        acc = 0
        n = len(word)
        for i in range(n):
            for j in range(i):
                s= word[j:i+1]
                if len(s)< k+4:
                    continue
                c = defaultdict(int)
                for a in s:
                    if a in vowls:
                        c[a] +=1
                    else:
                        c["b"] +=1
                if c["b"] ==k and all(c[a] >0 for a in vowls):
                    acc +=1
                
        return acc




#re =Solution().countOfSubstrings(word = "aeiou", k = 0)
#re =Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1)
re =Solution().countOfSubstrings(word = "iqeaouqi", k = 2)

#re =Solution().countOfSubstrings(word = "eioaua", k = 0)
print(re)