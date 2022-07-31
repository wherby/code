class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        n = len(edges)
        g=[[] for _ in range(n)]
        for i,a in enumerate(edges):
            if a >=0:
                g[i].append(a)
        def bfs(node):
            visited =[0]*n
            st =[node]
            idx = 0 
            dic ={}
            while st:
                tst =[]
                for a in st:
                    if visited[a] ==0:
                        visited[a] =1
                        dic[a]= idx 
                        for b in g[a]:
                            if visited[b] ==0:
                                tst.append(b)
                st =tst 
                idx +=1
            return dic
        dic1 = bfs(node1)
        dic2 = bfs(node2)
        mx = 10**9
        ret = -1
        for a in range(n):
            if a in dic1 and a in dic2:
                k = max(dic1[a],dic2[a])
                if k <mx:
                    ret =a 
                    mx = k 
                if k ==mx:
                    ret = min(ret,a)
        return ret




re =Solution().closestMeetingNode(edges = [5,3,1,0,2,4,5], node1 = 3, node2 = 2)
print(re)