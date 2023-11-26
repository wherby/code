# https://www.bilibili.com/video/BV1Rw411P72r/?spm_id_from=333.999.0.0&vd_source=ca787d3785cbd6247961eba27850fa0c
# https://leetcode.cn/contest/biweekly-contest-118/problems/find-maximum-non-decreasing-array-length/
# 单调队列优化dp
from typing import List, Tuple, Optional


from itertools import accumulate
from collections import defaultdict,deque
import math
INF  = math.inf

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        s= list(accumulate(nums,initial=0))
        n = len(nums)
        f = [0]*(n+1) # f[0] 表示空数组
        last = [0]*(n+1)
        q = deque([0])
        
        for i in range(1,n+1):
            # 1 在转移前，去掉队首无用数据
            while len(q) >1 and s[q[1]] + last[q[1]] <= s[i]:
                q.popleft()
                
            #2  转移 q[0]是最大的转移来源
            f[i] = f[q[0]] +1
            last[i] = s[i] - s[q[0]]
            
            # 把f入队前，去掉队尾无用数据
            while q and s[q[-1]] + last[q[-1]] >= s[i] + last[i]:
                q.pop()
            q.append(i)
        return f[n]

re =Solution().findMaximumLength([4,3,2,6])
print(re)




re =Solution().findMaximumLength([546,575,247,650,178,752,356,318,131,438])
print(re)