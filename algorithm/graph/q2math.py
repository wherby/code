#https://github.com/gzc/leetcode/blob/master/cpp/1001-10000/1811-1820/Maximum%20Number%20of%20Accepted%20Invitations.cpp
class Solution:
    def maximumInvitations(self,g):
        m = len(g)
        n = len(g[0])
        girls = [-1] *n

        def BipartiteMatch(g,u,visited,girls):
            for v in range(n):
                if g[u][v] == 0 or visited[v]:
                    continue

                visited[v] = True
                if girls[v] <0 or BipartiteMatch(g,girls[v],visited,girls):
                    girls[v] = u
                    return True
            return False    
        
        match =0
        for u in range(m):
            visted = [False] *n
            if BipartiteMatch(g,u,visted,girls):
                match +=1
        return match

grid = [[1,0,1,0],
               [1,0,0,0],
               [0,0,1,0],
               [1,1,1,0]]

re =Solution().maximumInvitations(grid)
print(re)