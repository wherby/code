# https://codeforces.com/gym/104064/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0117/solution/cf104064l.md
# 最大值为L的概率等于 小于等于L的概率 - 小于等于L-1 的概率， 容斥原理？ 用二维图像分析均匀分布的概率是符合的   （x+1)**2 - x**2  这时的差值就是 x+1 的边界面积
# 如果最大值小于i,则i的位置不变


import init_setting
from cflibs import *
def main(): 
    n, i, k = MII()
    ans = 0
    
    ans += ((i - 1) / n) ** k * i
    for M in range(i, n + 1):
        ans += ((M / n) ** k - ((M - 1) / n) ** k) * (M + 1) / 2
    
    print(ans)