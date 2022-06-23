class Solution:
    def cellsInRange(self, s: str) :
        nextc = lambda c : chr(ord(c)+1)
        c1, c2 = s[0], s[3]
        i1, i2 = int(s[1]), int(s[4])
        to_ret = []
        c = c1
        while c <= c2 :
            for i in range(i1, i2+1) :
                to_ret.append(c+str(i))
            c = nextc(c)
        return to_ret

re  = Solution().cellsInRange(s = "K1:L2")