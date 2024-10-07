# https://leetcode.cn/problems/gas-station/solutions/2933132/yong-zhe-xian-tu-zhi-guan-li-jie-pythonj-qccr/
from typing import List, Tuple, Optional

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = min_s= acc = 0
        for i,(g,c) in enumerate(zip(gas,cost)):
            acc += g-c 
            if acc <min_s:
                min_s =acc 
                ans = i+1
        return -1 if acc <0 else ans