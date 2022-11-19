# https://leetcode.com/contest/biweekly-contest-91/problems/split-message-based-on-limit/
##  https://leetcode.com/problems/split-message-based-on-limit/solutions/2807533/python-find-the-number-of-substrings/

class Solution:
    def splitMessage(self, s: str, limit: int):
        cur = k = i = 0
        while 3 + len(str(k)) * 2 < limit and cur + len(s) + (3 + len(str(k))) * k > limit * k:
            k += 1
            cur += len(str(k))
        res = []
        if 3 + len(str(k)) * 2 < limit:
            for j in range(1, k + 1):
                l = limit - (len(str(j)) + 3 + len(str(k)))
                res.append('%s<%s/%s>' % (s[i:i + l], j, k))
                i += l
        return res