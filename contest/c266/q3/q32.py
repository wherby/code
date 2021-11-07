class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        l=1
        r =100000
        def myDiv(a,b):
            return (a+b-1) //b
        def getNum(a):
            cnt = 0
            print(a)
            for q in quantities:
                re = myDiv(q,a)
                cnt += re
            return cnt
        while r >l:
            mid = (l+r)//2
            c = getNum(mid)
            if c >n:
                l= mid+1
            else:
                r = mid
        return l

Solution().minimizedMaximum(1,[1])