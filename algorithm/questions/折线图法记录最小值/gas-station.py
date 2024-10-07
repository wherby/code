# https://leetcode.cn/problems/gas-station/solutions/2933132/yong-zhe-xian-tu-zhi-guan-li-jie-pythonj-qccr/
from typing import List, Tuple, Optional
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ls = [a-b for a,b in zip(gas,cost)]
        if sum(ls)<0:
            return -1
        n = len(ls)
        l = 0 
        ls = ls +ls
        acc =0 
        for i in range(n):
            if i<l:continue 
            if ls[i]>=0:
                l = i 
                acc = 0
                for j in range(n):
                    acc += ls[i+j]
                    if acc <0:
                        l =i+j
                        break 
                if acc >=0 :
                    return i