# Ujimatsu_Chiya
# https://www.bilibili.com/video/BV17RwBeqErJ/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c
# 使用pow(self.fac[-1],-1,self.mod) 求出阶乘的逆元，再一次求低阶阶乘的逆元
from typing import List, Tuple, Optional
class COMB:
    def __init__(self, n=100000, mod=1000000007):
        self.N = n
        self.mod = mod
        self.fac = [0] * self.N
        self.finv = [0] * self.N
        self.fac[0] =  1
        for i in range(1, self.N ):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.finv[-1] = pow(self.fac[-1],-1,self.mod)
        for i in range(self.N-1,0,-1):
            self.finv[i-1] = self.finv[i ] *i % self.mod

    def C(self, n, m):
        return self.fac[n] * self.finv[n - m] % self.mod * self.finv[m] % self.mod

    def A(self, n, m):
        return self.fac[n] * self.finv[n - m] % self.mod


co = COMB()


class Solution:
    def minMaxSums(self, a: List[int], k: int) -> int:
        mod = 1000000007
        a.sort()
        n = len(a)
        ans = 0
        for i in range(n):
            right = n - 1 - i
            for j in range(min(right, k - 1) + 1):
                ans += co.C(right, j) * a[i]
            left = i
            for j in range(min(left, k - 1) + 1):
                ans += co.C(left, j) * a[i]
        return ans % mod


re =Solution().minMaxSums(a = [1,2,3], k = 2)

#re =Solution().minMaxSums(nums = [5,0,6], kk = 1)
print(re)