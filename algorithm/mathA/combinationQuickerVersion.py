#Will pass https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/submissions/594158648/https://leetcode.cn/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/submissions/594158648/

from typing import List, Tuple, Optional


# 预处理阶乘以及其逆元
max_n = int(1e5)
fac = [1] * (max_n+1)
facinv = [1] * (max_n+1)

MAX_NUM = int(1e9+7)
for i in range(1,max_n+1):
    fac[i] = fac[i-1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i],MAX_NUM-2,MAX_NUM)

def myComb(n,m):    
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n-m] % MAX_NUM
from collections import Counter
class Solution:
    def minMaxSums(self, nums: List[int], kk: int) -> int:
        nums.sort()
        mod = 10**9+7
        ret = 0
        n = len(nums)
        for i,a in enumerate(nums):
            for k1 in range(kk):
                ret += myComb(i,k1)*a 
                ret += myComb(n-i-1,k1)*a
        return ret %mod