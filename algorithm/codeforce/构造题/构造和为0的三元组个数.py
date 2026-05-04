# https://codeforces.com/gym/106511/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0501/solution/cf106511k.md
# 找到 n**3 和 n**2 的构造基组合 凑K 



import init_setting
from lib.cflibs import *
def main():
    k = II()
    
    for i in range(10000):
        if i * (i - 1) * (i - 2) // 6 > k:
            i -= 1
            k -= i * (i - 1) * (i - 2) // 6
            ans = [0] * i
            break
    
    cur = 1
    while k:
        v = math.isqrt(k)
    
        ans.append(4 * cur)
        ans.extend([-3 * cur] * v)
        ans.extend([-cur] * v)
    
        k -= v * v
        cur *= 10
    
    print(len(ans))
    if ans: print(*ans)