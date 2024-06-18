# https://leetcode.cn/contest/weekly-contest-402/problems/maximum-total-damage-with-spell-casting/description/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from heapq import heappop,heappush 

from collections import Counter


class DPWithBuffer:
    def __init__(self,gate) -> None:
        self.gate=gate
        self.hp = [(0,-19)]
        self.buff = deque([])
    
    def getMax(self,nxt):
        while self.buff and self.gate(self.buff[0][0],nxt):
            a,v = self.buff.popleft()
            heappush(self.hp,(-v,a))
        #print(self.hp)
        return -self.hp[0][0]
    
    def addBuff(self,bf):
        self.buff.append(bf)

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c= Counter(power)
        ks = list(c.keys())
        ks.sort()
        dic ={}
        for k in ks:
            dic[k] = k *c[k]
        dpBuff= DPWithBuffer(lambda x,y:x+2<y)
        mx = 0
        
        for k in ks:
            t = dpBuff.getMax(k)
            dpBuff.addBuff((k,t+ dic[k]))
            mx = max(mx,t+ dic[k])
        return mx




re =Solution().maximumTotalDamage(power = [1,1,3,4])
print(re)