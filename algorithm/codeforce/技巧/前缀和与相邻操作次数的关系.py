# https://codeforces.com/gym/106642/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0814/solution/cf106642b.md
# algorithm/codeforce/技巧/docs/前缀和与操作次数的关系.md

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k, x = MII()
    
        acc = [0] * (n + 1)
        
        for i in range(1, n + 1):
            l, r = fmax(-(n - i) * k, acc[i - 1] - k), fmax(0, acc[i - 1] + k)
            
            while l <= r:
                mid = (l + r) // 2
                
                start = -mid
                step = start // k
                
                if (start + start + step * (-k)) * (step + 1) // 2 <= x:
                    r = mid - 1
                else:
                    l = mid + 1
            
            acc[i] = l
            x += l
        
        outs.append(' '.join(str(acc[i + 1] - acc[i]) for i in range(n)))
    
    print('\n'.join(outs))