# https://codeforces.com/gym/104017/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0821/solution/cf104017j.md
# 这里需要求最大的因子，对于l,w 而言，需要构成的gcd 的数字  
# l1,w1,l2,w2   l1 +w1 + l2 +w2 = (l+m-2) *2
#  l-2 <=li <=l w-2<=wi<=w  
# 这里可以列举4个角是否加入对应的边的情况，得到所有边的组合，但是如果不是对称的情况，一定会出现3个不同的值？这样就会导致出现的GCD不如2个值？
# 但是3个不同的值的时候，有可能会出现GCD =2 的情况

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    def factors(x):
        for i in range(1, 100000):
            if i * i > x: break
            if x % i == 0:
                yield i
                if x // i != i:
                    yield x // i
    
    for _ in range(t):
        w, l = MII()
        
        ans = {2}
        
        for x in factors(math.gcd(w - 1, l - 1)): ans.add(x)
        for x in factors(math.gcd(w - 2, l)): ans.add(x)
        for x in factors(math.gcd(w, l - 2)): ans.add(x)
        
        ans = sorted(ans)
        
        outs.append(f'{len(ans)} {" ".join(map(str, ans))}')
    
    print('\n'.join(outs))