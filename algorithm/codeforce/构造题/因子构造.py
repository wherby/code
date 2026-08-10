# https://codeforces.com/gym/106632/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0805/solution/cf106632e.md
# 如果把矩阵先简化为一维矩阵，题目就变成了在连续 L 个数字中，至少有2个数字能被L整除
# 而自然数序列在L个数字中 只能保证有1个数字被L整除，所以这里采用了因子乘积构建，i*(i+1),这样就确定了一定有两个因子能被L整除

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        outs.append('YES')
    
        for i in range(1, n + 1):
            outs.append(' '.join(str((i + j) * (i + j + 1)) for j in range(m)))
    
    print('\n'.join(outs))