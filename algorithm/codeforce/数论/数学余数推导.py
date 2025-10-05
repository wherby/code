# https://codeforces.com/gym/104854/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1003/solution/cf104854c.md
# 利用 pb + 1 与 b+1, pb+2 与b+2 整除条件构造  p-1 ，(p-1)*2 与b+1,b+2 整除2的条件
# 然后在大的数轴空间搜索 k(b+1)(b+2) = 2*(p-1) 压缩空间为1/3指数空间  
 
import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        p = II()
        possible_bs = set()
        
        for b in range(1, 10 ** 6 + 1):
            if (p - 1) % (b + 1) == 0 and 2 * (p - 1) % (b + 2) == 0:
                possible_bs.add(b)
        
        for k in range(1, 2 * 10 ** 6 +  1):
            if 2 * (p - 1) % k == 0:
                v = 2 * (p - 1) // k
                b = (math.isqrt(4 * v + 1) - 1) // 2 - 1
                if b > 0 and (p - 1) % (b + 1) == 0 and 2 * (p - 1) % (b + 2) == 0:
                    possible_bs.add(b)
        
        possible_bs = sorted(possible_bs)
        outs.append(str(len(possible_bs)))
        outs.append(' '.join(map(str, possible_bs)))
    
    print('\n'.join(outs))