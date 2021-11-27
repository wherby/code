class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        m = len(n)
        res = []
        st =[]
        if n[0] != "-":
            for a in n :
                st.append(a)
            st.reverse()
            while st and x <= int(st[-1]):
                res.append(st[-1])
                st.pop()
            res.append(str(x))
            st.reverse()
            res = res + st
        else: 
            res.append("-")
            for a in range(1,m):
                st.append(n[a])
            st.reverse()
            while st and x >= int(st[-1]):
                res.append(st[-1])
                st.pop()
            res.append(str(x))
            st.reverse()
            res =res +st
        #print(res)
        return "".join(res)

re = Solution().maxValue(n = "-132", x = 3)
print(re)