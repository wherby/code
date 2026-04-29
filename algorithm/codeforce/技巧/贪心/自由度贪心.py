# https://codeforces.com/gym/106500/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0427/solution/cf106500b.md
# 首先 1..n 和 n+1 .. n*2 必须在两个不同的数组里，否则后半部分任一个到前半部分都不符合了
# 从大到小考虑前半部分的对应匹配， 每多一个前半部分的数字，则会多一个可选的数字自由度，但是还有一个自由度是剩下的数字，这两个自由度的小值才是当前可以选择的candidate数量

import init_setting
from cflibs import *
def main():
    n = II()
    ans = 1
    
    for i in range(1, n + 1):
        ans *= fmin(i, n - i + 1)
    
    print(ans)