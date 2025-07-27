# 子数组表示连续的数列
# 求非冲突子数列用枚举左维护右或者枚举右维护左
# 这里ls 维护了右端点的最小值和次小值，因为这里是删除一个限制,只有去除最小值，使用次小值才能有增益，所以增益就加在最小值上积累
# 如果有两个以上的最小值出现了，则增益变为0，直到有更小的最小值出现才会有新的增益到新的最小值
# https://leetcode.cn/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/3603047/mei-ju-zuo-duan-dian-wei-hu-zui-xiao-ci-4nvu6/?envType=daily-question&envId=2025-07-26
from typing import List, Tuple, Optional

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        gp=[[] for _ in range(n)]
        for a,b in conflictingPairs:
            if a > b:
                b,a = a,b 
            gp[a].append(b)
        
        ls = [n+1,n+1]
        extr= [0]*(n+2)
        ans = 0 
        for i in range(n,0,-1):
            ls.extend(gp[i])
            ls.sort()
            ls = ls[:2]
            ans += ls[0] -i 
            extr[ls[0]] += ls[1]-ls[0]
        return ans + max(extr)
