from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        cnt = 0
        tlen = sum([len(a) for a in words])
        w = words[0]
        sidx = ord(w[0]) - ord('a')
        eidx = ord(w[-1])- ord('a')
        @cache
        def dfs(i,start,end):
            if i == n:
                return 0
            w = words[i]
            sidx = ord(w[0]) - ord('a')
            eidx = ord(w[-1])- ord('a')
            #print(i,start,eidx,end,sidx,end==sidx,eidx ==start)
            ret = 0
            ret = max(ret,dfs(i+1,start,eidx) + (end==sidx))
            ret = max(ret,dfs(i+1,sidx,end) + (eidx ==start))
            return ret
        cnt = dfs(1,sidx,eidx)
        #print(cnt)
        return tlen - cnt




re =Solution().minimizeConcatenatedLength(words =["aaa","c","aba"])
print(re)