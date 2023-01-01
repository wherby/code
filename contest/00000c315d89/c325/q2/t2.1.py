# https://leetcode.cn/circle/discuss/RmydJj/

from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def checkCounter(cnt):
            for char in 'abc':
                if cnt[char] < k: return False
            return True
        n = len(s)
        tmp = s * 2
        l, r = 0, n
        cnt = Counter(s)
        if not checkCounter(cnt): return -1
        ans = n
        while l <= n:  ##
            while not checkCounter(cnt):
                cnt[tmp[r]] += 1
                r += 1
            ans = min(ans, r - l)
            cnt[tmp[l]] -= 1
            l += 1
        return ans