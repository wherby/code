# https://leetcode.cn/problems/sum-of-beauty-of-all-substrings/submissions/
# use counter as deafultdict(int)
from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            c = Counter()
            for j in range(i,n):
                c[s[j]] +=1
                cnt += max(c.values()) - min(c.values())
        return cnt