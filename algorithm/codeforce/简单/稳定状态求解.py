# https://codeforces.com/gym/106712/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0918/solution/c
# 进位稳定状态求解， 依靠一个足够长的序列，得到稳定状态


import init_setting
from lib.cflibs import *
def main():
    s = [int(c) for c in I()]
    n = len(s)
    s.reverse()
    
    for i in range(2 * n):
        s.append(0)
    
    for i in range(1, 3 * n):
        s[i] += s[i - 1]
    
    carry = 0
    for i in range(3 * n):
        s[i] += carry
        carry = s[i] // 10
        s[i] %= 10
    
    print(s[-1])