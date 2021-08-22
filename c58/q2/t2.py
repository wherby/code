class Solution:
    def checkMove(self, board, rMove, cMove, color) :
        if board[rMove][cMove] !=".":
            return False
        dirctions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        dColor =""
        if color=="B":
            dColor = "W"
        else:
            dColor = "B"
        find = False
        
        for d in dirctions:
            x =d[0]
            y = d[1]
            stage =0
            nextX = rMove + x 
            nextY = cMove +y
            #print(rMove,cMove,nextX,nextY)
            #print(dColor,board[nextX][nextY],nextX,nextY)
            while nextX >=0 and nextX <8 and nextY <8 and nextY >=0 and board[nextX][nextY] == dColor:
                nextX = nextX + x
                nextY = nextY +y
                stage =1
            #print(stage)
            if stage ==1 and  nextX >=0 and nextX <8 and nextY <8 and nextY >=0  and board[nextX][nextY] == color:
                find = True
        return find
            



board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
rMove = 4
cMove = 3
color = "B"
board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]
rMove = 4
cMove = 4
color = "W"
print(Solution().checkMove(board,rMove,cMove,color))