from collections import defaultdict
import functools
class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        @functools.lru_cache(None)
        def dp(i, j):
            if i == j:
                return {int(s[i])}
            res = {}
            for m in range(i + 1, j, 2):
                for a in dp(i, m - 1):
                    for b in dp(m + 1, j):
                        cur = a * b if s[m] == '*' else a + b
                        if cur <= 1000:  # opt with 0 <= answers[i] <= 1000
                            res[cur] = 2
            return res
        print(dp(0, len(s) - 1))
        res = {**dp(0, len(s) - 1), **{eval(s): 5}}
        return sum(res.get(a, 0) for a in answers)


re = Solution().scoreOfStudents("7+3*1*2", [20,13,42])
print(re)