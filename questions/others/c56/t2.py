class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = []
        queue.append([entrance[0],entrance[1],0])
        maze[entrance[0]][entrance[1]] = "+"
        while(len(queue)> 0):
            temp = queue.pop(0)
            for move in moves:
                x1 = temp[0] + move[0]
                y1 = temp[1] + move[1]
                if x1 >=0 and x1 <m and y1 >=0 and y1<n :
                    if maze[x1][y1] == ".":
                        queue.append([x1,y1,temp[2]+1])
                        maze[x1][y1]="+"
                        if x1 ==0 or x1 ==m-1 or y1 ==0 or y1 == n-1:
                            return temp[2]+1
        return -1

        

maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
entrance = [1,2]
a = Solution().nearestExit(maze,entrance)
print(a)
