# https://leetcode.cn/problems/count-stable-subarrays/solutions/3832945/fen-duan-er-fen-cha-zhao-qian-zhui-he-py-ukgs/
# 记录起点，使用 bisect_right
from typing import List, Tuple, Optional

from bisect import bisect_right,insort_left,bisect_left
from itertools import pairwise
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        ls = []
        start  = 0
        pls = [0]
        for i in range(n):
            if i ==n-1 or nums[i]> nums[i+1]:
                ls.append(start)
                m = i- start +1
                pls.append(pls[-1] + m*(m+1)//2)
                start= i+1

        ret = []
        for l, r in queries:
            k_s = bisect_right(ls, l) 
            k_e = bisect_right(ls, r) -1
            if k_s> k_e:
                ret.append((r-l+1)*(r-l+2)//2)
                continue
            cnt = pls[k_e] -pls[k_s]
            m1 = ls[k_s] - l 
            m2 = r - ls[k_e] +1 
            cnt += m1*(m1+1)//2 + m2*(m2+1)//2
            ret.append(cnt)
            
        return ret





re =Solution().countStableSubarrays(nums =[5,25,15,6], queries = [[1,3],[3,3]])
print(re)