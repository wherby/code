from collections import deque
# deque for priority queue, append and appendleft

d = {"^": (-1, 0),"v": (1, 0),"<": (0, -1),">": (0, 1)}
class Solution(object):
    def conveyorBelt(self, matrix, start, end):
        """
        :type matrix: List[str]
        :type start: List[int]
        :type end: List[int]
        :rtype: int
        """
        m,n = len(matrix),len(matrix[0])
        q = deque([(0,start[0],start[1])])
        book = [[10**9] * n for _ in range(m)]
        book[start[0]][start[1]]=0
        while q:
            t,x,y = q.popleft()
            if [x,y] ==end:
                return t
            for dr,(dx,dy) in d.items():
                nx,ny = x+dx, y +dy
                if not (0<=nx<m and 0<=ny<n):continue
                if dr == matrix[x][y]:
                    if book[nx][ny] <= t: continue
                    book[nx][ny] = t
                    q.appendleft((t,nx,ny))  # appendleft
                else:
                    if book[nx][ny] <= t+1: continue
                    book[nx][ny] = t+1
                    q.append((t+1,nx,ny))     #append
                    

re =Solution().conveyorBelt(matrix = [">>v","v^<","<><"], start = [0,1], end = [2,0])
print(re)