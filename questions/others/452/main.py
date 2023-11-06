class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        spoints = sorted(points, key=lambda x: x[1])
        endIndex = spoints[0][1]
        number = 1
        for i in range(1, len(spoints)):
            if endIndex >= spoints[i][0]:
                pass
            else:
                endIndex = spoints[i][1]
                number = number+1
        return number


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
s = Solution()
n = s.findMinArrowShots(points)
print(n)
