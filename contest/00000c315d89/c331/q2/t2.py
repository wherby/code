from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vos = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)
        acc = 0
        pre = [0]
        for i,a in enumerate(words):
            if a[0] in vos and a[-1] in vos:
                acc +=1
            pre.append(acc)
        res = []
        for a,b in queries:
            res.append(pre[b+1]-pre[a])
        return res





re =Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
print(re)