class Solution:
    def validTicTacToe(self, board: list[str]) -> bool:
        xs,os =0,0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "O":
                    os +=1
                if board[i][j] =="X":
                    xs +=1
        if os >xs:
            return False
        checks = 0
        for i in range(3):
            if board[i][0]==board[i][1] and board[i][2] == board[i][0] and board[i][0]=="O":
                checks +=1
            if board[0][i]==board[1][i] and board[2][i] == board[0][i] and board[0][i]=="O":
                checks +=1
            if board[0][0]==board[1][1] and board[2][2] == board[0][0] and board[0][0]=="O":
                checks +=1
            if board[2][0]==board[1][1] and board[0][2] == board[1][1] and board[1][1]=="O":
                checks +=1
        xchecks = 0
        for i in range(3):
            if board[i][0]==board[i][1] and board[i][2] == board[i][0] and board[i][0]=="X":
                xchecks +=1
            if board[0][i]==board[1][i] and board[2][i] == board[0][i] and board[0][i]=="X":
                xchecks +=1
            if board[0][0]==board[1][1] and board[2][2] == board[0][0] and board[0][0]=="X":
                xchecks +=1
            if board[2][0]==board[1][1] and board[0][2] == board[1][1] and board[1][1]=="X":
                xchecks +=1
        #print(xchecks,checks)
        if xchecks and xs ==os:
            return False
        
        if  checks  and xs > os:
            return False
        
        if xchecks and checks:
            return False
        
        if xs -1 > os:
            return False
        return True


re = Solution().validTicTacToe( board = ["X  ","X  ","O O"])
print(re)

        
