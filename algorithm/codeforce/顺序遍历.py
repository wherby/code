# https://codeforces.com/problemset/problem/662/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0508/solution/cf662d.md
# 其实算是遍历匹配每一位数字。 resid 是余数，如果不匹配，则一直增加最高位，因为其余位数已经匹配
from cflibs import *

def main():
    t = II()
    outs = []

    for _ in range(t):
        s = I()[4:]
        
        cur = 1988

        v10 = 1
        to_add = 1
        resid = 0

        for i in range(len(s) - 1, -1, -1):
            resid = resid + v10 * int(s[i])
            v10 *= 10
            
            cur += to_add
            while cur % v10 != resid:
                cur += to_add
            
            to_add *= 10
        
        outs.append(cur)

    print('\n'.join(map(str, outs)))