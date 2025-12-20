# Only precomute will pass
# https://leetcode.cn/contest/weekly-contest-374/problems/count-the-number-of-infection-sequences/submissions/
# contest\00000c361d112\c374\q4\t4 copy.py

MOD = 10**9+7
MX = 10**5
class Factorial:
    def __init__(self, MX,MOD=MOD):
        self.f = [1] * (MX + 1)
        self.g = [1] * (MX + 1)
        self.MOD = MOD
        for i in range(1, MX+1):
            self.f[i] = self.f[i-1] * i % MOD
        self.g[-1] = pow(self.f[-1], MOD-2, MOD)
        for i in range(MX-1, -1, -1):
            self.g[i] = self.g[i+1] * (i+1) % MOD

    def fact(self, n):
        return self.f[n]

    def fac_inv(self, n):
        return self.g[n]

    def perm(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[n-m] % self.MOD

    def comb(self, n, m):
        if m < 0 or n < 0 or n < m: return 0
        return self.f[n] * self.g[m] * self.g[n-m] % self.MOD

    def catalan(self, n):
        return (self.comb(2*n, n) - self.comb(2*n, n-1)) % self.MOD

    def inv(self, n):
        return self.f[n-1] * self.g[n] % self.MOD

if __name__ == '__main__':
    fact = Factorial(MX)