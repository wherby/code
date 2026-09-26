# https://codeforces.com/gym/105055/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0910/solution/cf105055b.md
# 所有的状态装换图，这里的奇偶性与初始长度有关，
# 这里是每人k轮，则与初始情况的余数和奇偶性有关
# 如果长度是奇数，则后手一定能使得达到余0的操作;如果初始余数是0，长度是偶数，先手不能变成余数是2，则后手能变成余数是0
# 如果长度是偶数，且初始余数不等于0，则先手一定等让余数变2，后手则只能让余数变成 1,2

import init_setting
from cflibs import *
def main():
    n, k = MII()
    s = [int(c) for c in I()]
    
    cur = 0
    
    for x in s:
        cur = (2 * cur + x) % 3
    
    if cur == 0 or n % 2: print('JULIA')
    else: print('GIOVANA')