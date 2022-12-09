# https://leetcode.cn/problems/delivering-boxes-from-storage-to-ports/solution/cong-cang-ku-dao-ma-tou-yun-shu-xiang-zi-4uya/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        p,w, neg,W = [0]*(n+1) ,[0]*(n+1),[0]*(n+1) ,[0]*(n+1)
        
        for i in range(1,n+1):
            p[i],w[i]  = boxes[i-1]
            if i >1:
                neg[i] = neg[i-1] + (p[i-1] !=p[i])
            W[i] = W[i-1] + w[i]
        
        opt  =deque([0])
        f,g = [0]*(n+1) ,[0]*(n+1)
        for i in range(1,n+1):
            while i- opt[0] > maxBoxes or W[i] - W[opt[0]] > maxWeight:
                opt.popleft()
            
            f[i] = g[opt[0]] + neg[i] +2
            if i != n:
                g[i] = f[i] - neg[i+1]
                while opt and g[i] <= g[opt[-1]]:
                    opt.pop()
                opt.append(i)
        return f[n]

re  =Solution().boxDelivering(boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3)
print(re)

            
