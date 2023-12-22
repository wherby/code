# https://leetcode.cn/problems/beautiful-towers-ii
from typing import List, Tuple, Optional
class Solution:
    def maximumSumOfHeights(self, hs: List[int]) -> int:
        n = len(hs)
        def getls(hs):
            st =[]
            ls = []
            for i,a in enumerate(hs):
                while st and a <hs[st[-1]]:
                    st.pop()
                if st:
                    ls.append(ls[st[-1]] + a*(i-st[-1]))
                else:
                    ls.append(a*(i+1))
                st.append(i)
            return ls
        left = getls(hs)
        right = getls(hs[::-1])[::-1]
        mx = 0
        for i in range(n):
            mx = max(mx,left[i] + right[i] -hs[i])
        return mx
    
re =Solution().maximumSumOfHeights([5,3,4,1,1])
print(re)