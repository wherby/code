
# https://codeforces.com/gym/106598/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0908/solution/cf106598m.md
# algorithm/string/docs/Chen-Fox-Lyndon定理.md
# 循环字符串比较大小
# 字典序传递性（Lexicographical Monotonicity）：
# 在 Lyndon 理论中，如果 $st < ts$，则对任意 $p, q \ge 1$，都有 $s^p t^q < t^q s^p$。

import init_setting
from cflibs import *
def main():
    s1, s2 = LI()
    p, q = MII()
    
    if not p or not q: print('=')
    else:
        v1 = s1 + s2
        v2 = s2 + s1
        
        if v1 < v2: print('<')
        elif v1 > v2: print('>')
        else: print('=')