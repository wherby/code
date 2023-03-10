from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dic={}
        dic[0] = 1
        res = defaultdict(int)
        #res[0]=1
        mod=10**9+7
        for v,k in types:
            res = defaultdict(int)
            for i in range(0,min(target//k +1,v)+1):
                for k1,v1 in dic.items():
                    if k1 + i*k <=target:
                        res[k1 + i*k] += v1
                        res[k1 + i*k] %=mod 
            dic =res 
            #print(dic)
        return dic[target]




types=[[6,1],[49,2],[33,3],[26,4],[28,5],[45,6],[4,7],[23,8],[46,9],[39,10],[12,11],[28,12],[37,13],[18,14],[10,15],[27,16],[26,17],[10,18],[34,19],[11,20],[35,21],[5,22],[47,23],[19,24],[15,25],[27,26],[50,27],[3,28],[24,29],[18,30],[49,31],[32,32],[18,33],[5,34],[34,35]]
re =Solution().waysToReachTarget(target = 500, types =types)
print(re)