# Ujimatsu_Chiya
# https://leetcode.cn/contest/weekly-contest-433/ranking/?region=local_v2
from typing import List, Tuple, Optional
class COMB:
    def __init__(self, n=100000, mod=1000000007):
        self.N = n
        self.mod = mod
        self.fac = [0] * (n + 1)
        self.inv = [0] * (n + 1)
        self.finv = [0] * (n + 1)
        self.fac[0] = self.fac[1] = self.inv[1] = self.finv[0] = self.finv[1] = 1
        for i in range(2, self.N + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = (self.mod - self.mod // i) * self.inv[self.mod % i] % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

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