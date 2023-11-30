# https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/description/

# using stack

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def minimumCoins(self, ps: List[int]) -> int:
        n = len(ps) 
        dq = deque([(0,n+1)])
        
        for i in range(n,0,-1):
            # 弹出离开窗口
            while dq and i*2 +1 < dq[-1][1]:
                dq.pop()
            
            # 转移
            f = dq[-1][0] + ps[i-1]
            
            # 加入队首
            while f <= dq[0][0]:
                dq.popleft()
            
            dq.appendleft((f,i))
        return dq[0][0]

re =Solution().minimumCoins([1,10,1,1])
print(re)