# https://leetcode.com/contest/weekly-contest-485/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/description/
# 从左到右遍历的时候，去掉一定应该去掉的签名的值
# 从右到左遍历的时候，去掉右边重复值
from typing import List, Tuple, Optional


from collections import Counter
class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        c = Counter(s)
        st = []

        for a in s:
            while st and a <st[-1] and c[st[-1]]>1:
                d = st.pop()
                c[d] -=1
            st.append(a)
        while st and c[st[-1]]>1:
            d=st.pop()
            c[d] -=1
        return "".join(st)





re =Solution().lexSmallestAfterDeletion("aabcdfdbcbk")
print(re)