# https://codeforces.com/problemset/problem/670/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0908/solution/cf670e.md
# 用两堆栈模拟编译器，在寻找删除pair的时候，用累加值求pair点。

import init_setting
from cflibs import *
def main():
    n, m, p = MII()
    s1 = [1 if c == '(' else -1 for c in I()]
    s2 = []
    
    while len(s1) > p:
        s2.append(s1.pop())
    
    for c in I():
        if c == 'R':
            s1.append(s2.pop())
        elif c == 'L':
            s2.append(s1.pop())
        else:
            c = s1.pop()
            if c == 1:
                while c:
                    c += s2.pop()
            else:
                while c:
                    c += s1.pop()
            if s2:
                s1.append(s2.pop())
    
    while s2:
        s1.append(s2.pop())
    
    print(''.join('(' if c == 1 else ')' for c in s1))