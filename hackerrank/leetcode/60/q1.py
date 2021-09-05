#Flood 4 Direct search
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """		
        def flood(x,y,color,t,re,image):
        	if re[x][y] != 0:
        		return
        	re[x][y] =color
        	if(x >0 and image[x-1][y] ==t):
        		flood(x-1,y,color,t,re,image)
        	if(y >0 and image[x][y-1] ==t):
        		flood(x,y-1,color,t,re,image)
        	if(x+1<n and image[x+1][y] ==t):
        		flood(x+1,y,color,t,re,image)
        	if(y+1<m and image[x][y+1] ==t):
        		flood(x,y+1,color,t,re,image)
        t =image[sr][sc]
        re =[]
        n =len(image)
        m =0
        for im in image:
        	m = len(im)
        	re.append([0]*m)

        flood(sr,sc,newColor,t,re,image)
        for i in range(n):
        	for j in range(m):
        		if re[i][j] ==0:
        			re[i][j] = image[i][j]

     
        return re


s = Solution()
image=[[0,0,0],[0,0,1]]
s.floodFill(image,1,1,2)