from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def oddString(self, words: List[str]) -> str:
        dic= defaultdict(list)
        for word in words:
            n = len(word)
            ls = [ord(word[i])-ord(word[i+1]) for i in range(n-1)]
            dic[tuple(ls)].append(word)
        #print(dic)
        for k,v in dic.items():
            if len(v) == 1:
                return v[0]





re =Solution().oddString(words = ["adc","wzy","abc"])
print(re)