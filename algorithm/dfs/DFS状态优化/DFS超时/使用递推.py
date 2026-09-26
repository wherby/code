# “DP 状态转移优化”、“前缀和优化 DP”
# 首先把区间改成[i:j) 左开右闭区间，这样更好维护INDEX
# 这里因为在求 pre_max 中需要维护一个 最大的 dp[i][k] + sum(i:k)， 所以加上pre[k] 求最大值，再减去pr[i]，这里i是一个固定的值是可以做到的
# 但是在求suf_max[q][j]的时候，由于 suf_max[q][j] 中 属于q :j 中最小的值 所以suf_max 中递推dp[i][j] - pre[i] 这时i 相对是变话的，这样就减去了一个变化值， 通过"先吸收变化量、后统一补偿"的方式
# 其实 pre_max ,suf_max 在维护的时候，直接维护 sum区间的值也是可行的
# 这里其实是在循环中维护suf_max,在遍历的时候维护前缀 pre_max ： “动态规划 + 前缀/后缀最值优化”

from typing import List, Tuple, Optional
from functools import cache
from math import inf
class Solution:
    def stoneGameV(self, sv: List[int]) -> int:
        pre =[0]
        n = len(sv)
        for a in sv:
            pre.append(a+pre[-1])
        dp =[[0]*(n+1) for _ in range(n)]
        suf_max = [[-inf]*(n+1) for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            suf_max[i][i+1] = -pre[i]
            pre_max = 0 
            k = i+1 
            for j in range(i+2,n+1):
                while k <j and pre[k] -pre[i] <= pre[j] - pre[k]:
                    pre_max = max(pre_max, dp[i][k] + pre[k])
                    k+=1
                
                q = k if pre[k-1] - pre[i] != pre[j] - pre[k-1] else k-1 
                
                dp[i][j] = max(pre_max - pre[i] ,suf_max[q][j] + pre[j])
                
                suf_max[i][j] = max(suf_max[i+1][j], dp[i][j] - pre[i])
        return dp[0][n]
    
from input import nums
re = Solution().stoneGameV(nums)
print(re)  
            