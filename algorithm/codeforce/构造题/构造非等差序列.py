# https://codeforces.com/gym/103828/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0827/solution/cf103828l.md
# 这里把多维的问题，变换为一维问题子问题
# 1 到 n 组成序列，构成非等差序列
# 首先可以把序列分成奇数和偶数部分： 由于奇数和偶数的分割点不能形成等差数列，所以在奇数和偶数部分再继续2分，递归得到1大小的子区间，因为在递归的时候可以知道每个子区间之间连接不能构成等差序列，所以所形成的数组就不存在差序列
# 下面证明奇数和偶数连接区间不形成等差序列，如果形成3长度的等差序列，则首位奇偶性一致，则不可能。
# 在遍历子区间的时候，使用缩放数轴，一直保持了区间的整数连续性。


import init_setting

from cflibs import *
def main():
    def f(x):
        if x == 1: return [0]
        return [2 * v for v in f(x - x // 2)] + [2 * v + 1 for v in f(x // 2)]
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        v = f(n)
        
        for i in range(n):
            outs.append(' '.join(str(v[i] * n + v[j] + 1) for j in range(n)))
    
    print('\n'.join(outs))