from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumDeletions(self, word: str, klimit: int) -> int:
        dic = defaultdict(int)
        for a in word:
            dic[a] +=1
        m = len(dic)
        dicF =defaultdict(int)
        for _,v in dic.items():
            dicF[v] += v
        ls = []
        kys = []
        for f,v in dicF.items():
            ls.append((f,v))
            kys.append(f)
        ls.sort()
        sm = len(word)
        ret = sm
        for k in kys:
            acc =0
            for k1 in kys:
                if k1 <k:continue
                if k<=k1<=k + klimit:
                    acc += dicF[k1]
                else:
                    acc += dicF[k1] //k1*(k+klimit)
            ret = min(ret,sm -acc)
        return ret






re =Solution().minimumDeletions(word = "dabdcbdcdcd", klimit = 2)
print(re)