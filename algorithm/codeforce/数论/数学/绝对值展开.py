# https://codeforces.com/gym/105394/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0922/solution/cf105394d.md
# (1-p )**abs(x-i)
# p = (1 - round(float(p) * 1000000) * pow(1000000, mod - 2, mod)) % mod. 是（1-q) 在mod 意义下的整数值
# q = 1/p 
#  x<i    i- x       ; x >=i    x -i 
# 所以可以把对x的查询分为 大于x 和小于x 两部分
# 对于小于x的 取 p**i 的前缀和 再乘 q**x 
# 对于大于x的 取 q**i 的后缀和 再乘 p**i  
# 代码中前后缀命名相反？  
# 如果 rsum 不是 sum(right) - sum(left-1)  
#.    是 sum(right) - sum(left) 则 fen_pre.rsum(idx, n) 在idx点上的积累  是0 因为idx点上的值会被减去 ，   fen_suf.rsum(0, idx) 在 idx点上积累也是0 因为 fen_suf.add(idx + 1, x * rev_pows[idx] % mod)
import init_setting
from cflibs import *
from lib.fenwicktree import FenwickTree
def main():
    mod = 10 ** 9 + 7
    
    n, q, p = LI()
    n = int(n)
    q = int(q)
    p = (1 - round(float(p) * 1000000) * pow(1000000, mod - 2, mod)) % mod
    
    pows = [1] * (n + 2)
    for i in range(1, n + 2):
        pows[i] = pows[i - 1] * p % mod
    
    revp = pow(p, mod - 2, mod)
    
    rev_pows = [1] * (n + 2)
    for i in range(1, n + 2):
        rev_pows[i] = rev_pows[i - 1] * revp % mod
    
    fen_pre = FenwickTree(n + 1)
    fen_suf = FenwickTree(n + 1)
    
    outs = []
    for _ in range(q):
        query = LI()
        if query[0] == '+':
            x = int(query[1])
            idx = int(query[2]) - 1
    
            fen_pre.add(idx, x * pows[idx] % mod)
            fen_suf.add(idx + 1, x * rev_pows[idx] % mod)
            
        elif query[0] == '-':
            x = int(query[1])
            idx = int(query[2]) - 1
            
            fen_pre.add(idx, -x * pows[idx] % mod)
            fen_suf.add(idx + 1, -x * rev_pows[idx] % mod)
        
        else:
            idx = int(query[1]) - 1
            
            ans = 0
            ans += fen_pre.rsum(idx, n) % mod * rev_pows[idx] % mod
            ans += fen_suf.rsum(0, idx) % mod * pows[idx] % mod
            outs.append(ans % mod)
    
    print('\n'.join(map(str, outs)))

main()