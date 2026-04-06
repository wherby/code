# https://codeforces.com/gym/106439/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0327/solution/cf106439m.md
# (𝑎 mod 𝑏) +(𝑏 mod 𝑎)=(𝑎|𝑏)
# a=b 显然不可能。
# 如果 a<b ，则左侧等于 a+b mod a 这个数显然小于 2a 。
# 而如果 b 的最高位比 a 大，则 a|b 超过了 a+2a的最高位>2a 矛盾。而 b 大于 a ，所以两个数最高位是相等的。
# 所以 b mod a=b−a ，因此我们只需求 b=a|b 且 b 的最高位等于 a 的最高位的元素对数。考虑枚举 b ，则 a 不超过 min(n,b−1) 
# ，最高位与 b 的最高位相同，且 a|b=b ，即 a 是 b 的子集。这个 a 的数量可以用类似数位 DP 的方式解决。也可以理解为小于 x 的二进制数有多少个的统计。具体可见后面的代码。
# a>b 的情况完全对称，这里不作叙述。
# 使用 v = x & -x  取得x的最低位 
# 如果可以当前位填1，则所有低位都可以填，此时低位有 1<<j  种填法，但是要减去 1 ，因为低位都是0的填法在最开始已经计算了，但是这时加上该位为1，低位为0 的那1种填法， 刚好又成了 1<<j
# for j in range(len(vals) - 2, -1, -1):
    # if cur + vals[j] <= m_bound:
    #     cur += vals[j]
    #     ans += 1 << j
# sub-question ： 已知 a<b 且 a,b的最高位相等，a|b == b,   且a < m 的个数有多少个 


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        ans = 0
        
        for i in range(1, n + 1):
            m_bound = fmin(i - 1, m)
            x = i
            vals = []
    
            while x:
                v = x & -x
                vals.append(v)
                x -= v
            
            if m_bound < vals[-1]: continue
            
            cur = vals[-1]
            ans += 1  # 只取最高位的情况
            
            for j in range(len(vals) - 2, -1, -1):
                if cur + vals[j] <= m_bound:
                    cur += vals[j]
                    ans += 1 << j
        
        n, m = m, n
        
        for i in range(1, n + 1):
            m_bound = fmin(i - 1, m)
            x = i
            vals = []
    
            while x:
                v = x & -x
                vals.append(v)
                x -= v
            
            if m_bound < vals[-1]: continue
            
            cur = vals[-1]
            ans += 1
            
            for i in range(len(vals) - 2, -1, -1):
                if cur + vals[i] <= m_bound:
                    cur += vals[i]
                    ans += 1 << i
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))