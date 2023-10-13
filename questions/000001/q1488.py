# https://leetcode.cn/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2023-10-13
from typing import List, Tuple, Optional
from collections import defaultdict,deque
from sortedcontainers import SortedDict,SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        n = len(rains)
        st = defaultdict(int)
        ret = [-1]*(n+1)
        cand = SortedList([])
        for i,a in enumerate(rains,1):
            #print(i,a,rains)
            if a >0:
                if st[a] >0:
                    #print(i,a ,len(cand),cand)
                    idx = cand.bisect_left(st[a])
                    if len(cand) ==0 or idx>= len(cand):
                        return []
                    b = cand[idx]
                    cand.remove(cand[idx])
                    ret[b] = a 
                    st[a] =i
                else:
                    st[a] =i
            else:
                cand.add(i)
            #print(cand,ret,a, st)
        for b in cand:
            ret[b] =1
        return ret[1:]
    
re = Solution().avoidFlood([0,1,1])
print(re)