# https://codeforces.com/gym/105786/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1223/solution/cf105786j.md
# 在DP过程中,需要把小区间合并为大区间,这时区间的对象产生了变换,这里用了建立新的区间List的方式,把不同的区间合并,变成同一形状的区间合并
# 在区间合并的时候,需要知道合并的值是多少,这时候,用了l,r记录了合并最小cost对应的平台的左右端点,在合并的时候,最佳值端点有可能在ls[i] 或者 rs[i]对应的点，所以需要循环两次找到可能的左右端点



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    inf = 10 ** 18
    def f(x, l, r, c):
        if l <= x <= r: return c
        if x < l: return l - x + c
        return x - r + c
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ls = nums[:]
        rs = nums[:]
        cost = [0] * n
        
        while len(ls) > 1:
            nls, nrs, ncost = [], [], []
            
            for i in range(0, len(ls), 4):
                l, r, cur = 0, 0, inf
                
                for j in range(i, i + 4):
                    v = 0
                    for k in range(i, i + 4):
                        v += f(ls[j], ls[k], rs[k], cost[k])
                    
                    if v < cur:
                        cur = v
                        l = ls[j]
                        r = ls[j]
                    elif v == cur:
                        l = fmin(l, ls[j])
                        r = fmax(r, ls[j])
                    
                    v = 0
                    for k in range(i, i + 4):
                        v += f(rs[j], ls[k], rs[k], cost[k])
                    
                    if v < cur:
                        cur = v
                        l = rs[j]
                        r = rs[j]
                    elif v == cur:
                        l = fmin(l, rs[j])
                        r = fmax(r, rs[j])
                
                nls.append(l)
                nrs.append(r)
                ncost.append(cur)
            
            ls = nls
            rs = nrs
            cost = ncost
        
        outs.append(f(0, ls[0], rs[0], cost[0]))
    
    print('\n'.join(map(str, outs)))