from typing import List, Tuple, Optional
from collections import defaultdict,deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        dic = defaultdict(list) 
        for i,route in enumerate(routes):
            for a in route:
                dic[a].append(i)
        visit={}
        cand =[source]
        cnt = 0
        while cand:
            tmp =[]
            
            for a in cand:
                if a == target:
                    return cnt 
                if a in visit:
                    continue
                visit[a] = 1
                for idx in dic[a]:
                    for b in routes[idx]:
                        if b not in visit:
                            tmp.append(b)
                    routes[idx]= {}
            cand = tmp
            cnt +=1
        return -1


re = Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
print(re)