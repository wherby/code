# https://codeforces.com/gym/106160/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1105/solution/cf106160a.md
# 利用对称消去，计算每个位数的贡献度

import init_setting
from cflibs import *
def main(): 
    n = [int(c) for c in I()]
    k = len(n)
    
    ans = 0
    val = 0
    cur = 1
    
    for i in range(k - 1):
        val += n[i] * cur
        ans += val
        cur = cur / 10
    
    val += n[-1] * cur
    print(ans * 0.9 + val)

main()