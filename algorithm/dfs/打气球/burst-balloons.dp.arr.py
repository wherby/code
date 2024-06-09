from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [1]+nums+[1]   
        f = [[0] * (n + 2) for _ in range(n + 2)]
        
        for i in range(n-1,-1,-1): ## 一定要左端点 从大到小， 使得长度是从小到大
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    f[i][j] =max(f[i][j],f[i][k]+ f[k][j] + ls[i]*ls[k]*ls[j])
        return f[0][n+1]

re =Solution().maxCoins([3,1,5,8])
print(re)