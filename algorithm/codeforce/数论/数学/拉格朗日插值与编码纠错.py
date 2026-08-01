# https://codeforces.com/gym/106628/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0729/solution/cf106628l.md
# algorithm/codeforce/docs/数论/拉格朗日插值与编码纠错.md


import init_setting
from cflibs import *
def main():
    mod = 10 ** 9 + 7
    k = II()
    
    xs = []
    ys = []
    
    for _ in range(k + 2):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    saved_vals = [0] * (k + 2)
    
    for i in range(k + 2):
        val = 1
        
        for j in range(k + 2):
            if i == j: continue
            val = val * (mod + xs[i] - xs[j]) % mod
        
        saved_vals[i] = ys[i] * pow(val, -1, mod) % mod
    
    for i in range(k + 2):
        val = 0
        
        for j in range(k + 2):
            if i == j: continue
            val += saved_vals[j] * (mod + xs[i] - xs[j]) % mod
            val %= mod
        
        if val == 0:
            ans = 0
            for j in range(k + 2):
                if j != i:
                    A = ys[j]
                    B = 1
                    for v in range(k + 2):
                        if v != i and v != j:
                            A = A * (mod - xs[v]) % mod
                            B = B * (mod + xs[j] - xs[v]) % mod
                    ans += A * pow(B, -1, mod) % mod
                    ans %= mod
            print(ans)
            break