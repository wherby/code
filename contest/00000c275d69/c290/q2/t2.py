class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        cnt = 0 
        n = len(circles)
        for i in range(202):
            for j in range(202):
                isFind = False
                for k in range(n):
                    x,y,r = circles[k]
                    if (x-i)**2 + (y-j)**2 <= r**2+0.1:
                        isFind =True
                        break
                if isFind:
                    cnt +=1
        return cnt
    
re =Solution().countLatticePoints([[2,2,2],[3,4,1]])
print(re)
        
