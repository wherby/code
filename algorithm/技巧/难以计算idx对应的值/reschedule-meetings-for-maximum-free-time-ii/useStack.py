# 由于pre 和post 计算之后和当前idx对应不好做匹配
# 所有先计算所有post，由于第一个元素的时候，前面两个post对应的值不能使用，则pop两次
# 对于pre的计算也是这样，直接延迟两个idx计算当前最大的pre值

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
        post =[0]
        for a in ls[::-1]:
            post.append(max(post[-1],a))
        post.pop()
        post.pop()
        mx = 0
        pre = 0
        #print(pre,post,ls)
        for i in range(1,n-1):
            a = endTime[i] - startTime[i]
            
            mx = max(mx, ls[i-1]+ ls[i])
            #print(a,mx,i)
            if a <= pre  or a <= post[-1]:
                mx = max(startTime[i+1]-endTime[i-1],mx)
            if i >0:
                pre = max(pre,ls[i-1])
            post.pop()
        return mx

re = Solution().maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5])
print(re)