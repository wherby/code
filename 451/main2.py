from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        a = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = [x*i for x, i in a]

        return "".join(res)


a = Solution()
a.frequencySort("tree")
