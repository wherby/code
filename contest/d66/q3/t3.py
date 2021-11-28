class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        x,y = startPos
        x1,y1 = homePos
        if x ==x1 and y ==y1 :
            return 0
        cost =0
        if x >x1:
            while x >x1:
                x -=1
                cost+= rowCosts[x]
        if x < x1:
            while x < x1:
                x += 1
                cost += rowCosts[x]
        if y > y1:
            while y > y1:
                y -=1
                cost += colCosts[y]
        if y < y1:
            while y < y1:
                y +=1
                cost += colCosts[y]
        return cost

re = Solution().minCost(startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]) 
print(re)