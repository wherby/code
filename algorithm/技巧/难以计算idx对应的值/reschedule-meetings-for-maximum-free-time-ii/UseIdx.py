# https://leetcode.cn/problems/reschedule-meetings-for-maximum-free-time-ii/?envType=daily-question&envId=2025-07-10
from typing import List, Tuple, Optional
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime = [0]+startTime+[eventTime]
        endTime = [0] + endTime+ [eventTime]
        n = len(startTime)
        ls = []
        for i in range(1,n):
            ls.append(startTime[i] - endTime[i-1])
        m = len(ls)
        pre = [0]*n 
        post = [0]*n 
        for i in range(n-2):
            pre[i+2] = max(pre[i+1],ls[i]) # 当前值会影响延迟2 
            post[-i-2] = max(post[-1-i], ls[-i-1]) # ls的 -i-1 对应 post 的 -i-2 ，第一项post对应的是ls[2] 所以post[1]
        mx = 0
        print(pre,post,ls)
        for i in range(1,n-1):
            a = endTime[i] - startTime[i]
            
            mx = max(mx, ls[i-1]+ ls[i])
            #print(a,mx,i)
            if a <= pre[i]  or a <= post[i+1]:
                mx = max(startTime[i+1]-endTime[i-1],mx)
        return mx

re = Solution().maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5])
print(re)