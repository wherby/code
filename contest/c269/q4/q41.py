from collections import defaultdict
class Node:
    def __init__(self, n):
        self.parent = self
        self.rank = 0

class DisjointSet:  # with rank and path compression
    def __init__(self, elements):
        self.sets = [Node(n) for n in elements]
        self.count = len(self.sets)
        
    def find(self, element):
        n = self.sets[element]
        path_node = []
        while n.parent != n:
            n = n.parent
            path_node.append(n) # 記錄路上的 nodes

        # path compression
        for v in path_node:
            v.parent = n
        return n
        
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            # 把 rank 小的掛到 rank 大的下方
            if u.rank < v.rank:
                u.parent = v
            else:
                v.parent = u
                if v.rank == u.rank:
                    u.rank += 1
            self.count -= 1

    def count_sets(self):
        return self.count


class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        dsu = DisjointSet(list(range(n)))
        reMeeting = []
        dsu.union(0,firstPerson)
        dic =defaultdict(list)
        for x,y,t in meetings:
            dic[t].append((t,x,y))
            reMeeting.append((t,x,y))
        reMeeting.sort()
        #print(reMeeting)
        def dfs(x,g,vist):
            for y in g[x]:
                dsu.union(x,y)
                if vist[y] ==0:
                    vist[y] =1
                    dfs(y,g,vist)
        for t,x,y in reMeeting:
            if dsu.find(x) == dsu.find(0) or dsu.find(y) ==dsu.find(0) :
                rls = dic[t]
                if len(rls) >0:
                    del dic[t]
                    
                    g = defaultdict(list)
                    for _,x1,y1 in rls:
                        g[x1].append(y1)
                        g[y1].append(x1)
                    vist =defaultdict(int)
                    dfs(x,g,vist)
                    dfs(y,g,vist)
                     

                if dsu.find(x) != dsu.find(y):
                    dsu.union(x,y)

        res = []
        for i in range(n):
            if dsu.find(i) == dsu.find(0) or dsu.find(i) == dsu.find(firstPerson):
                res.append(i)
        
        return res

re = Solution().findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1)
print(re)