from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        ret = -1
        sm = sum(skill)
        hf = n //2 
        if sm%hf != 0:
            return -1 
        tt= sm //hf
        dir = defaultdict(list)
        for i,a in enumerate(skill):
            dir[a].append(i)
        vist = {}
        acc =0
        for i in range(n):
            if i in vist:continue
            vist[i] = 1 
            fd =False
            while dir[tt-skill[i]]:
                a = dir[tt-skill[i]].pop()
                if a in vist: continue
                else: 
                    vist[a] =1 
                    acc += skill[i]*(tt-skill[i])
                    fd = True
                    break
                
            if fd == False:return -1 
        return acc
        
        




re =Solution().dividePlayers([3,2,5,1,3,4])
print(re)