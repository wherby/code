import collections
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sc = collections.Counter(s)
        stc =collections.Counter(t+s)
        sm =0
        for a in stc:
            t1 = stc[a]
            t2 = sc[a]
            sm += abs(t2*2-t1)
        return sm

re = Solution().minSteps(s = "leetcode", t = "coats")
print(re)