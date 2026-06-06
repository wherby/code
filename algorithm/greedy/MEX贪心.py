# https://leetcode.cn/contest/weekly-contest-504/problems/lexicographically-maximum-mex-array/
# MEX 贪心
from typing import List, Tuple, Optional


from collections import Counter
class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        cur = 0
        res = []
        n = len(nums)
        while cur <n:
            cur_mex = 0 
            while c[cur_mex] >0:
                cur_mex +=1
            if cur_mex ==0 :
                return res + [0]*(n-cur +1)
            st = set()
            while cur < n:
                a= nums[cur]
                c[a] -=1
                if a < cur_mex:
                    st.add(a)
                cur +=1
                if len(st) == cur_mex:
                    break
            res.append(cur_mex)
        return res





re =Solution()
print(re)