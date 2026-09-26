# https://codeforces.com/gym/106682/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0903/solution/cf106682d.md
# 把111111的基础问题变成 999999的问题之后，每位的求解就能直接求解
# 然后利用一个结论，就是每个一样的货币有10个就能进位，这样就化简得到最终的 ： 这里是错误的，比如 110 就需要10个 11组合，
# 但是这样想是错误的 algorithm/codeforce/技巧/docs/错误贪心.md
# 反而需要先乘 9 
# 这里怎么理解？ 为什么只有 s[i+1] ==1 的时候才减去1 ？ 防止在处理第i位的时候，从个位上来的进位导致了i位进位到i+1位了，溢出错误


import init_setting
from cflibs import *
def main():
    s = [int(c) for c in I()]
    s.reverse()

    n = len(s)
    carry = 0

    for i in range(n):
        s[i] = s[i] * 9 + carry
        carry = s[i] // 10
        s[i] %= 10

    if carry: s.append(carry)
    s.append(0)

    n = len(s)
    ans = 0

    for i in range(n - 1, -1, -1):
        while s[i]:
            ans += 1
            s[0] += 1
            
            for j in range(n):
                if s[j] >= 10:
                    s[j + 1] += s[j] // 10
                    s[j] %= 10
                else:
                    break
            
            if s[i + 1] == 1: s[i + 1] -= 1
            else: s[i] -= 1

    print(ans)