# https://codeforces.com/gym/104479/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1129/solution/cf104479j.md
# 此题分两个阶段， 第一阶段，使用贪心方式求得最大的排列数，在求最大的排列数的同时把每位上能取的最大值也求出来
# 因为对于当前位而言，选取最小的数字一定能让它前面的数字的排列值最大，所以在选择让它前面的排列值最大不变的情况下，此位置的值越大越好，并记录下来作为边界
# 再用DP求数量的时候，  st_range = sorted(range(n), key=lambda x: ans[x])
# 排列之后的顺序就是每个Set 的位置，在DP的时候，每个阶段选择又会是下一阶段选择的条件
# 因为上一个状态已经记录，对每个 j 遍历的时候， res 记录了当前j 能从上一个状态转移的状态数，并且同时用  lsts[i][j]  作为状态记录点
# 因为 j 在增大的同时，当前值一定能包含上一个j的状态值，所以res就可以当做"前缀和”
# for j in range(l):
        # if lsts[i][j] > ans[i]: break
        
        # while pt < len(cur) and (cur[pt] < lsts[i][j] or (cur[pt] == lsts[i][j] and last_i < i)):

import init_setting
from cflibs import *
from lib.fenwicktree import *

def main(): 
    rnd = random.getrandbits(30)
    
    n = II()
    lsts = []
    vals = []
    
    for _ in range(n):
        l = II()
        nums = [x + rnd for x in MII()]
        nums.sort()    
        lsts.append(nums)
        vals.extend(nums)
    
    vals = sorted(set(vals))
    k = len(vals)
    d = {v: i for i, v in enumerate(vals)}
    
    fen = FenwickTree(k)
    ans = []
    
    for i in range(n):
        l = len(lsts[i])
        
        val = fen.rsum(d[lsts[i][0]] + 1, k - 1)
        chosen = lsts[i][0]
        
        for j in range(1, l):
            if fen.rsum(d[lsts[i][j]] + 1, k - 1) != val: break
            chosen = lsts[i][j]
    
        fen.add(d[chosen], 1)
        ans.append(chosen)
    
    st_range = sorted(range(n), key=lambda x: ans[x])
    
    last_i = n
    cur = [0]
    dp = [1]
    
    mod = 998244353
    
    for i in st_range:
        ncur = []
        ndp = []
        
        pt = 0
        res = 0
        
        l = len(lsts[i])
        for j in range(l):
            if lsts[i][j] > ans[i]: break
            
            while pt < len(cur) and (cur[pt] < lsts[i][j] or (cur[pt] == lsts[i][j] and last_i < i)):
                res += dp[pt]
                res %= mod
                pt += 1
            
            ncur.append(lsts[i][j])
            ndp.append(res)
        
        cur = ncur
        dp = ndp
        last_i = i
    
    print(sum(dp) % mod)

main()