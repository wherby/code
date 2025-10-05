# https://codeforces.com/gym/105822/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1004/solution/cf105822c.md
# 在总体奇偶性满足的条件下，生成满奇偶性要求的数字和，使得消耗的数字是连续的
# 奇偶性判定时候，可以考虑奇数个数，也可以考虑偶数个数。偶数的时候看分配规律则可以得到(数型结合)


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        s = I()
        if s.count('E') % 2: outs.append('NO')
        else:
            outs.append('YES')
            pt1 = 1
            pt2 = 2
            
            for i in range(n):
                if s[i] == 'O':
                    outs.append(f'{pt1} {pt2}')
                    pt1 += 2
                    pt2 += 2
                elif pt1 < pt2:
                    outs.append(f'{pt1} {pt1 + 2}')
                    pt1 += 4
                else:
                    outs.append(f'{pt2} {pt2 + 2}')
                    pt2 += 4
    
    print('\n'.join(outs))