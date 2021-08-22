class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        lss = []
        for i in range(numRows):
            lss.append([0]*n)
        dirction = [[0, 1], [1, -1]]
        x = 0
        y = 0
        v = dirction[0]
        for char in s:
            lss[y][x] = char
            if v == dirction[0] and y == numRows-1:
                v = dirction[1]
            if v == dirction[1] and y == 0:
                v = dirction[0]
            x = x + v[0]
            y = y + v[1]
        res = []
        for i in range(numRows):
            for c in lss[i]:
                if c != 0:
                    res.append(c)
        return "".join(res)


s = Solution()
re = s.convert("AB", 1)
print(re)
