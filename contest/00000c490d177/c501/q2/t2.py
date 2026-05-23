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
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        dic = defaultdict(int)
        tmp =[]
        small_letters = set(map(chr, range(ord('a'), ord('z')+1)))
        word = "".join(chunks)
        
        for i,a in enumerate(word):
            if a in small_letters:
                tmp.append(a)
            elif a =="-" and (0<i<len(word)-1 and word[i-1] in small_letters and word[i+1] in small_letters):
                tmp.append(a) 
            else:
                if len(tmp):
                    t= "".join(tmp)
                    dic[t]+=1
                    tmp=[]
        if len(tmp):
            t= "".join(tmp)
            dic[t]+=1
            tmp=[]
        ret = []
        for q in queries:
            ret.append(dic[q])
        return ret 




re =Solution().countWordOccurrences( chunks = ["m  cq-i "], queries = ["m","cq-i","nm"])
#re =Solution().countWordOccurrences( chunks = ["oa  -j","-i- "], queries = ["oa","q","ad","j-is","j-i"])
print(re)