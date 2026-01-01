# https://codeforces.com/gym/105805/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1226/solution/cf105805d.md

import init_setting
from cflibs import *
from lib.fenwicktree import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        fen = FenwickTree(n + 1)
        ans = 0
        diff = []
        
        for x in nums:
            v1 = fen.rsum(x + 1, n)
            v2 = fen.rsum(0, x - 1)
            
            ans += v1
            diff.append(v2 - v1)
            
            fen.add(x, 1)
    
        diff.sort()
        
        res = [ans]
        
        for x in diff:
            res.append(res[-1] + x)
        
        outs.append(' '.join(map(str, res)))
    
    print('\n'.join(outs))

main()