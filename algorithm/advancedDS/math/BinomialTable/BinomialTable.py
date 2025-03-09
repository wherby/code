# https://atcoder.jp/contests/arc192/editorial/12202

class BinomialTable:
    def __init__(self, table_size):
        self.fact = [1] * table_size
        self.inv = [1] * table_size
        for i in range(1, table_size):
            self.fact[i] = self.fact[i - 1] * i % MOD
        self.inv[-1] = pow(self.fact[-1], -1, MOD)
        for i in reversed(range(1, table_size)):
            self.inv[i - 1] = self.inv[i] * i % MOD
    def binom(self, h, w):
        if h < 0 or w < 0:
            return 0
        return (self.fact[h + w] * self.inv[h] % MOD * self.inv[w]) % MOD
    def binom_sum(self, h, w):
        if h < 0 or w < 0:
            return 0
        return (self.binom(h + 1, w + 1) - 1) % MOD
    def binom_sum_sum(self, h, w):
        if h < 0 or w < 0:
            return 0
        return (self.binom(h + 2, w + 2) - (h + 2) * (w + 2) - 1) % MOD
MOD = 998244353
table = BinomialTable(3000000)
W, H, L, R, D, U = map(int, input().split())
ans = (table.binom_sum_sum(W, H) - table.binom_sum_sum(R - L, U - D)) % MOD
for i in range(D, U + 1):
    ans -= table.binom_sum(L - 1, i) * table.binom_sum(W - L, H - i)
    ans %= MOD
for i in range(L, R + 1):
    ans -= table.binom_sum(i, D - 1) * table.binom_sum(W - i, H - D)
    ans %= MOD
for i in range(D, U + 1):
    ans -= table.binom_sum(R - L, i - D) * table.binom_sum(W - R - 1, H - i)
    ans %= MOD
for i in range(L, R + 1):
    ans -= table.binom_sum(i - L, U - D) * table.binom_sum(W - i, H - U - 1)
    ans %= MOD
print(ans % MOD)
