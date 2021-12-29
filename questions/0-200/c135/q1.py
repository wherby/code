class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        ls = []
        for a,b in points:
            ls.append((a,b))
        if ls[0][0] == ls[1][0] == ls[2][0]:
            return False
        if ls[0][1] == ls[1][1] == ls[2][1]:
            return False
        xEqual= 0
        ls = list(set(ls))
        if len(ls) ==2:
            return False
        ls.sort()
        #print(ls)
        for i in range(1,3):
            if ls[i][0] == ls[i-1][0]:
                xEqual+=1
        if xEqual ==1:
            return True
        k1 = (ls[2][1]-ls[1][1]) /(ls[2][0] - ls[1][0])
        k2 = (ls[2][1]-ls[0][1]) /(ls[2][0] - ls[0][0])
        return k1 != k2



re = Solution().isBoomerang([[0,1],[1,2],[2,2]])
print(re)
