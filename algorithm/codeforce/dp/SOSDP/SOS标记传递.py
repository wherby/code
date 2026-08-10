# https://codeforces.com/gym/106631/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0803/solution/cf106631g.md
# 在把l,r 统一成一个形式之后，就只有l范围标记，但是l 会形成各种不同的二进制区间与x 形成的组合是不同的
# 所以用二进制视角，把l所形成的二进制区间上计算与x 形成的影响贡献
# 而在完整的二进制区间内，影响会均匀分步 ，这里采用SOS的传递方式，遍历所有状态空间，把状态从有当前位的状态传递到没有当前位的状态
# SOS DP 保证传递性，使得每个子状态只能传播一次 algorithm/dp/SOSDP/SOSDP传递性/每个子状态只传递一次.py 


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        bounds = []
        xs = []
        vs = []
        
        for _ in range(q):
            l, r, x, v = MII()
            
            bounds.append(l)
            xs.append(x)
            vs.append(-v)
            
            bounds.append(r + 1)
            xs.append(x)
            vs.append(v)
        
        
        ans = [0] * n
    
        for i in range(19, -1, -1):
            higher_msk = ~((1 << (i + 1)) - 1)
            cur_bit = 1 << i
            
            for j in range(2 * q):
                if bounds[j] & cur_bit:
                    higher = bounds[j] & higher_msk & xs[j]
                    lower = xs[j] & (cur_bit - 1)
                    ans[higher + lower] += vs[j] << i - lower.bit_count()
            
            for j in range(n):
                if j & cur_bit:
                    ans[j ^ cur_bit] += ans[j]
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))