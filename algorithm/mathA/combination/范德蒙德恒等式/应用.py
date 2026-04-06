# https://leetcode.cn/problems/direction-assignments-with-exactly-k-visible-people/description/
# 这个题目就是 范德蒙德恒等式 (Vandermonde's Identity) 的应用
# 怎么理解 范德蒙德恒等式 (Vandermonde's Identity) 的求和合并？ 对于需要看到k个人，则需要在n-1个里选择k个被看到
# 则就是comb(n-1,k) ,对于pos而言没有意义，在选择的k个中，如果在左边则是R 在右边则是L，没有选中的则相反。
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
comb = COMB(10**5)
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9+7
        
        return comb.C(n-1,k)*2%mod