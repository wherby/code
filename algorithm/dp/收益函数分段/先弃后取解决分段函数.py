# https://leetcode.cn/contest/weekly-contest-521/problems/maximize-meeting-earnings-with-idle-gaps/description/
# 这里收益函数是v和之前的间隔，如果没有之前值的话，间隔收益为0 
# 这里采用先弃后取的方式， 把end 先减去，然后在计算收益的时候加上 start就有了间隔收益
# 这里列举DP转移方程。可以把统一坐标的计算一起解决
# https://leetcode.cn/problems/maximize-meeting-earnings-with-idle-gaps/solutions/4035319/dong-tai-gui-hua-shi-zi-bian-xing-python-ycfm/
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key= lambda x:x[1])
        n = len(meetings)
        dp = [0]*n 
        ends = []
        diff = []
        ans = 0
        for i in range(n):
            start,end,v = meetings[i]
            dp[i] = v 
            idx = bisect_right(ends,start) -1 
            if idx >=0:
                dp[i] = max(dp[i] , diff[idx] + start + v )
            ans =max(ans,dp[i])
            
            cur = dp[i] -end
            pre = diff[-1] if diff else -10**20
            ends.append(end)
            diff.append(max(pre,cur))
        return ans
            
        




re =Solution().maxEarnings( meetings = [[3,5,4],[4,7,8],[8,10,3]])
print(re)