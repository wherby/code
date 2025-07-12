
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
            pre[i+2] = max(pre[i+1],ls[i])
            post[-i-2] = max(post[-1-i], ls[-i-1]) 
        mx = 0
        print(pre,post,ls)
        for i in range(1,n-1):
            a = endTime[i] - startTime[i]
            
            mx = max(mx, ls[i-1]+ ls[i])
            print(a,mx,i)
            if a <= pre[i]  or a <= post[i+1]:
                mx = max(startTime[i+1]-endTime[i-1],mx)
        return mx

re = Solution().maxFreeTime(eventTime = 34, startTime = [0,17], endTime = [14,19])
print(re)