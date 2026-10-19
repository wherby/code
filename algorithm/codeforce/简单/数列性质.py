# https://codeforces.com/gym/102307/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1010/solution/cf102307k.md
# 问题是求 Fibonacci 数列 的数字满足：
# 两项的奇偶性不同 ： Fibonacci 的奇偶性是 ：
# 斐波那契数列的奇偶规律是：奇、奇、偶循环。
# 即：F₁奇, F₂奇, F₃偶, F₄奇, F₅奇, F₆偶……     所以每3项有一项不符合，
# 两项的和也是 Fibonacci 数列的值 <= 这里暗示了这两项一定是相邻项
# 斐波那契性质：gcd(Fₘ, Fₙ) = F_gcd(m,n)  这里 m,n 是相邻的，gcd(m,n)=1
# 这里如果是普通数列, n个数字，相邻项是 n-1 ,但是Fibonacci 数列 f1==f2 ==1 ,只有里可以都和f2组合，所以总的是有n个pair备选

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        outs.append(n - (n + 1) // 3 if n >= 3 else 0)
    
    print('\n'.join(map(str, outs)))