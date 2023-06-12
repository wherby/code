class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        mx = m*n 
        st = [[0]*n for _ in range(m)]
        def findNextStart():
            for i in range(m):
                for j in range(n):
                    if st[i][j] == 0 :
                        return (i,j)
            return (m,0)
        
        def dfs(step):
            nonlocal mx
            i,j = findNextStart()
            #print(i,j,st)
            if i ==m:
                mx = min(mx,step)
            if step >= mx:
                return 
            mm = min(m-i,n-j)
            #print(mm)
            for i1 in range(mm,0,-1):
                isGood = True
                for i2 in range(i1):
                    for i3 in range(i1):
                        if st[i+i2][j+i3] != 0:
                            isGood =False
                            break
                if isGood:
                    for i2 in range(i1):
                        for i3 in range(i1):
                            st[i+i2][j+i3] = 1
                    dfs(step+1)
                    for i2 in range(i1):
                        for i3 in range(i1):
                            st[i+i2][j+i3] = 0
        dfs(0)
        return mx

re =Solution().tilingRectangle(11,13)
print(re)