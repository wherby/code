from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [1]+nums+[1]   
        f = [[0] * (n + 2) for _ in range(n + 2)]
        
        for l in range(1,n+1):# l 表示长度
            for i in range(0,n-l+1):# i 表示线段左边界连接的点
                j = i+l+1
                for k in range(i+1,j):
                    f[i][j] =max(f[i][j],f[i][k]+ f[k][j] + ls[i]*ls[k]*ls[j])
        return f[0][n+1]

re =Solution().maxCoins([3,1,5,8])
print(re)