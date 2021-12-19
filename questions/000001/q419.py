class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m,n = len(board),len(board[0])
        visited = [[0]* n  for _ in range(m)]
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j):
            visited[i][j] = 1
            for d in dir:
                x1,y1 = i + d[0],j+d[1]
                if x1>=0 and x1<m  and y1>=0 and y1<n and board[x1][y1] =="X" and visited[x1][y1] ==0:
                    dfs(x1,y1)
            

        cnt =0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and board[i][j] == "X":
                    dfs(i,j)
                    cnt +=1
        return cnt
        