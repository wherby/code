# https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/solutions/2790603/fen-zhi-si-xiang-xian-duan-shu-pythonjav-xnhz/?envType=daily-question&envId=2024-10-31
from typing import List, Tuple, Optional

class SegTree:
    def __init__(self,nums) -> None:
        n = len(nums)
        self.n = n
        self.nums = nums
        self.t = [[0] * 4 for _ in range(2 << n.bit_length())]

    def maintain(self, o):
        a, b = self.t[o * 2], self.t[o * 2 + 1]
        self.t[o] = self._merge(a,b)
        
    def _merge(self,a,b):
        c = [0]*4
        c[0] = max(a[0] + b[2], a[1] + b[0])
        c[1] = max(a[0] + b[3], a[1] + b[1])
        c[2] = max(a[2] + b[2], a[3] + b[0])
        c[3] = max(a[2] + b[3], a[3] + b[1])
        return c
    def build(self, o: int, l: int, r: int) -> None:
            if l == r:
                self.t[o][3] = max(self.nums[l], 0)
                return
            m = (l + r) // 2
            self.build(o * 2, l, m)
            self.build(o * 2 + 1, m + 1, r)
            self.maintain(o)

                # 把 nums[i] 改成 val
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.t[o][3] = max(val, 0)
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.maintain(o)

    def query(self,start,end):
        return self._query(1,0,self.n-1,start,end)

    def _query(self,o,l,r,qs,qe):
        if qs <=l and qe>=r:
            return self.t[o]
        if qs > r or qe < l:
            return [0]*4
        m = (l+r) //2
        left = self._query(o*2,l,m,qs,qe)
        right = self._query(o*2+1,m+1,r,qs,qe)
        return self._merge(left,right)
        

        

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        st = SegTree(nums)
        n = len(nums)
        st.build(1, 0, n - 1)

        ans = 0
        for i, x in queries:
            st.update(1, 0, n - 1, i, x)
            ans +=st.query(0,n-1)[3]
        return ans % 1_000_000_007

#作者：灵茶山艾府
#链接：https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/solutions/2790603/fen-zhi-si-xiang-xian-duan-shu-pythonjav-xnhz/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。#
    
re= Solution().maximumSumSubsequence([4,0,-1,-2,3,1,-1],[[3,1],[0,-2],[1,-1],[0,-2],[5,4],[6,-3],[6,-2],[2,-1]])
print(re)