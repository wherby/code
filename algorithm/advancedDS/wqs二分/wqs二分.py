# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/
# 这里有很多注意的细节，ans =max(ans, res + mid*k) 反而是错误的答案，而且这个更新是需要在 cnt >=n的时候更新
# 这样写也不对： 
# if cnt <=k:
#                 ans = max(ans,res + mid*cnt)
#                 print(mid,ans,res,cnt)
# 对于输入 k=2, [3,3,5,0,0,3,1,4]  mid =3,的 时候，只能检测到1次交易 
# WQS 二分是在规定了一次交易的“固定损耗（手续费）”的情况下，让市场自发选择能带来最高净收益的交易次数。
# 在转移的时候 >= 会捕获共线的交点，只有这样才能使得 cnt>=k的时候能得到边界值的最大的收益。因为二分的判断是cnt>=k的时候记录边界值

from typing import List, Tuple, Optional

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        l, r = 0,max(prices)
        
        def check(mid):
            dp0,cnt0  = -prices[0],0 
            dp1,cnt1 = 0,0 

            for i in range(1,n):
                prev_dp0, prev_cnt0 = dp0, cnt0
                prev_dp1, prev_cnt1 = dp1, cnt1
                
                # 买入：从昨天的空仓状态转移
                if prev_dp1 - prices[i] >= dp0:
                    dp0 = prev_dp1 - prices[i]
                    cnt0 = prev_cnt1
                
                # 卖出：从昨天的持有状态转移
                if prev_dp0 + prices[i] - mid >= dp1:
                    dp1 = prev_dp0 + prices[i] - mid
                    cnt1 = prev_cnt0 + 1

            return dp1,cnt1 
        ans = -1
        while l <=r:
            mid = (l+r)>>1
            res,cnt = check(mid)
            if cnt >=k:
                ans = res + mid*k
                l = mid+1
            else:  
                r =mid-1
        if ans ==-1:
            ans = sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        return ans