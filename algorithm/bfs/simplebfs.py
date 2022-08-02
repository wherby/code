# https://leetcode.cn/contest/weekly-contest-304/problems/find-closest-node-to-given-two-nodes/ 
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