# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/solutions/2031995/on-shuang-zhi-zhen-by-endlesscheng-4g9p/?envType=daily-question&envId=2024-09-27
from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if any(cnt[a] <k for a in "abc"):
            return -1 

        mx = left = 0 
        for i,a in enumerate(s):
            cnt[a] -=1
            while cnt[a] <k:
                cnt[s[left]] +=1
                left +=1
            mx = max(mx, i -left +1)
        return len(s) -mx