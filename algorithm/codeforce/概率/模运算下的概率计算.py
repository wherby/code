# https://codeforces.com/gym/106414/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0506/solution/cf106414l.md
# 用贡献法，维护经过n轮候 i 不出现的概率
# 在模运算（Modular Arithmetic）的语境下，mod + 1 - x 实际上就是数学上的 1 - x。在概率计算中，如果你已知某个事件不发生的概率是 x，那么该事件发生的概率就是 1 - x。
# 为什么要加上 mod？
# 在编程中（尤其是使用 Python, C++, Java 等），直接计算 1 - x 可能会得到一个负数。
# 使用x-y轴的统计变换，求取期望值
# algorithm/技巧/等价转换/x-y轴统计变换.md


import init_setting
from cflibs import *

def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        
        not_vis_prob = [1] * (n + 1)
        
        for _ in range(n):
            a, p, q = MII()
            not_vis_prob[a] = not_vis_prob[a] * (q - p) % mod * pow(q, -1, mod) % mod
        
        cur = 1
        ans = 0
        
        for x in not_vis_prob:
            cur = cur * (mod + 1 - x) % mod
            ans = (ans + cur) % mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))