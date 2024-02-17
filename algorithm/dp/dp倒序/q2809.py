# https://leetcode.cn/problems/minimum-time-to-make-array-sum-at-most-x/solutions/2607454/shi-shu-zu-he-xiao-yu-deng-yu-x-de-zui-s-fufg/?envType=daily-question&envId=2024-01-19
 
from typing import List, Tuple, Optional


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        ls = [(b,a) for a,b in zip(nums1,nums2)]
        ls.sort()
        #ls.sort()
        #print(ls)
        f  = [0]*(n+1)
        for i,(b,a) in enumerate(ls):
            for j in range(i+1,0, -1):
                ## 在 i 没有加入前，第j天的最大值是什么。
                f[j] = max(f[j],f[j-1] + a + b*j)  ## DP 倒序 j 表示是第j天的时候能消去最大值，通过外层i 的循环，把所有可能性包含
        
        s1 = sum(nums1)
        s2 = sum(nums2)
        print(f)
        for t,v in enumerate(f):
            if s1 + s2*t -v <= x:
                return t 
        return -1

re = Solution().minimumTime([4,4,9,10],[4,4,1,3],16)
print(re)