# https://codeforces.com/gym/105876/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0211/solution/cf105876b.md
# 构造最小字典序的permutation，使得前缀xor不为0，贪心构造


import init_setting
from cflibs import *
def main(): 
    n = II()
    if n % 4 == 3: print(-1)
    else:
        ans = list(range(1, n + 1))
        
        for i in range(3, n, 4):
            ans[i - 1], ans[i] = ans[i], ans[i - 1]
        
        print(*ans)