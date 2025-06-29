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
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        if len(words) <=2:
            return [0]*len(words)
        def getLs(word1,word2):
            acc = 0 
            for a,b in zip(word1,word2):
                if a ==b:
                    acc +=1
                else:
                    break
            return acc
        sl = SortedList([])
        
        n = len(words)
        words.append("*")
        dic ={}
        for i in range(n+1):
            t= getLs(words[i-1],words[i])
            sl.add((t,i-1,i))
            dic[(i-1,i)]=t
        ret = []
        for i in range(n):
            t1 = dic[(i-1,i)]
            t2 = dic[(i,i+1)]
            t3 = getLs(words[i-1],words[i+1])
            sl.remove((t1,i-1,i))
            sl.remove((t2,i,i+1))
            ret.append(max(t3,sl[-1][0]))
            sl.add((t1,i-1,i))
            sl.add((t2,i,i+1))
        return ret




re =Solution().longestCommonPrefix(["jump","run","run","jump","run"])
print(re)