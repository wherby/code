class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        color = [[[0]*3 for _ in range(N)] for _ in  range(N)]
        q = []
        for i in range(1,N):
            for t in range(1,3):
                color[0][i][t] =1
                q.append((0,i,t))
                color[i][i][t] =2
                q.append((i,i,t))
        while q:
            curStatus= q.pop()
            cat,mouse,turn =curStatus 
            
            for prevStatus in self.findAllPrevStatus(graph,curStatus):
                c,m,t =prevStatus
                if color[c][m][t] != 0:continue
                if color[cat][mouse][turn] == 3-turn:
                    color[c][m][t] =t
                    q.append(prevStatus)
                elif self.allNeighboursWin(color,graph,prevStatus):
                    color[c][m][t] = 3 -prevStatus[2]
                    q.append(prevStatus)
        return color[1][2][1]
    

    def findAllPrevStatus(self,graph,curstatus):
        ret = []
        mouse,cat,turn = curstatus
        if turn  ==1:
            for prevCat in graph[cat]:
                if prevCat ==0: continue
                ret.append((mouse,prevCat,2))
        else:
            for preMouse in graph[mouse]:
                ret.append((preMouse,cat,1))
        return ret

    def allNeighboursWin(self,color,graph,status):
        mouse,cat,turn = status
        if turn ==1:
            for nextMouse in graph[mouse]:
                if color[nextMouse][cat][2] != 2:
                    return False
        elif turn ==2:
            for nextCat in graph[cat]:
                if nextCat ==0: continue
                if color[mouse][nextCat][1] !=1:
                    return False
        return True 