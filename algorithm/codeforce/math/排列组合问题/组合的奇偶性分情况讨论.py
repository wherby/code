# https://codeforces.com/gym/106495/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0425/solution/cf106495j.md
# 三个数最终和的奇偶性，可以用组成此数的奇偶讨论的到可行的组合



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        c0 = n // 2
        c1 = (n + 1) // 2
        outs.append((math.comb(c0, 3) + math.comb(c1, 2) * c0) % mod)
    
    print('\n'.join(map(str, outs)))