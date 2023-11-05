class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        mx =0
        start =0
        startIdx = 1

        restrictions.sort()
        #print(restrictions)
        m =len(restrictions)
        for i in range(m):
            a,b = restrictions[i]
            bt = min(b,start + a- startIdx)
            startIdx = a
            start = bt
            restrictions[i][1] = bt
        for i in range(m-2,-1,-1):
            a,b = restrictions[i]
            startIdx,start = restrictions[i+1]
            bt = min(b,start+startIdx-a)
            restrictions[i][1] = bt
        start =0
        startIdx = 1
        a =startIdx
        b = start
        mx =0
        for a,b in restrictions:
            mt = (a -startIdx - abs(b-start))//2
            mx = max(mx, max(b,start) + mt)
            start=b
            startIdx =a
        #print(b,a,n)
        mx = max(mx, b+ n-a)
        return mx

re = Solution().maxBuilding(n = 6, restrictions = [])
print(re)