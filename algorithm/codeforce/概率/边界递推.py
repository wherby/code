# https://codeforces.com/gym/104009/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0321/solution/cf104009h.md
# 利用边界条件递推
# 每次可以推断下一次的概率， 但是如果K比较大，可能需要很多次才能获得下次策略的改变，所以需要基于不动点递推计算最多停留的次数到下一个阶段 algorithm/codeforce/docs/利用不动点计算当前停留的次数.md
# 利用不动点的二分，使得每次计算都在不同的策略方式进行的


import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    
    vals = []
    weights = []
    
    for _ in range(n):
        v, w = MII()
        vals.append(v)
        weights.append(w)
    
    st_range = sorted(range(n), key=lambda x: vals[x])
    
    acc_total = [0]
    acc_weights = [0]
    
    for i in st_range:
        v = vals[i]
        w = weights[i]
        
        acc_total.append(acc_total[-1] + v * w)
        acc_weights.append(acc_weights[-1] + w)
    
    ans = acc_total[n] / acc_weights[n]
    
    while k:
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[st_range[mid]] > ans: r = mid - 1
            else: l = mid + 1
        
        cur = l
        prob = acc_weights[cur] / acc_weights[n]      # 拒绝区间的概率
        to_add = (acc_total[n] - acc_total[cur]) / acc_weights[n] # 接受区间的期望值？
        
        v = to_add / (1 - prob) # 线性变换的不动点（也是当次数趋于无穷大时的极限期望值）
        
        l, r = 1, k
        while l <= r:
            mid = (l + r) // 2
            nans = pow(prob, mid) * (ans - v) + v
            if nans > vals[st_range[cur]]: r = mid - 1
            else: l = mid + 1
        
        cur = fmin(l, k)
        k -= cur
        ans = pow(prob, cur) * (ans - v) + v
    
    print(ans)