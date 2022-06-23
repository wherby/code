class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        g = [[0]*n for _ in range(n)]
        for x,y in dig:
            g[x][y] =1
        cnt = 0
        for x1,y1,x2,y2 in artifacts:
            isG =True
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if g[i][j] ==0:
                        isG = False
            if isG :
                cnt +=1
        return cnt