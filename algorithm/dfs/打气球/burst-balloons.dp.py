from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        ls = [1]+nums+[1]   
        dic = defaultdict(int)
        
        for i in range(n-1,-1,-1): ## 一定要左端点 从大到小， 使得长度是从小到大
            for j in range(i+2,n+2):
                for k in range(i+1,j):
                    dic[(i,j)] =max(dic[(i,j)], dic[(i,k)] + dic[(k,j)] + ls[i]*ls[k]*ls[j])
        return dic[(0,n+1)]

re =Solution().maxCoins([3,1,5,8])
print(re)