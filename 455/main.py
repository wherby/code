class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        sg = sorted(g)
        ss = sorted(s)
        re = 0
        gindex = 0
        for i in ss:
            if i >= sg[gindex]:
                re = re + 1
                gindex = gindex + 1
            else:
                pass
            if gindex >= len(sg):
                break
        return re


g = [1, 2]
s = [1, 2, 3]
s1 = Solution()
re = s1.findContentChildren(g, s)
print(re)
