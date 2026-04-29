# https://codeforces.com/gym/106500/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0428/solution/cf106500j.md
# 首先分情况讨论a==b ，然后在a==b 的正常路径下，v的取值是可变的，所以可以直接得到参与人数的答案
# 在a!=b 的情况， v=x+2y 优胜x和获奖y 的人数是固定值，题目中有限制 x+y<=n 所以求出的值 x+y的下限要小于n 


import init_setting
from cflibs import *
def main():
    a = II()
    b = II()
    c = II()
    d = II()
    
    if a == b:
        if c != d: print(0)
        else:
            v = 2 * c // (2 * a + 1)
            print(c - a * v)
    else:
        if (d - c) % (b - a): print(0)
        else:
            v = (d - c) // (b - a)
            if v < 0: print(0)
            elif c - a * v < (v + 1) // 2: print(0)
            else: print(c - a * v)