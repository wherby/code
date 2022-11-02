from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        dic = defaultdict(int)
        dic2 = {}
        for i in range(n):
            c = creators[i]
            id = ids[i]
            v = views[i]
            dic[c] += v 
            if c not in dic2:
                dic2[c] = (v,id) 
            else:
                vt,idv = dic2[c]
                if vt <v :
                    dic2[c] = (v,id)
                elif vt == v and idv> id:
                    dic2[c] = (v,id)
        mx = 0 
        cls = []
        vmax = max(dic.values())
        for k,v in dic.items():
            if v == vmax:
                cls.append([k,dic2[k][1]])
        return cls




re =Solution().mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4])
print(re)