# https://leetcode.cn/contest/weekly-contest-284/problems/minimum-weighted-subgraph-with-the-required-paths/
#给你一个整数 n ，它表示一个 带权有向 图的节点数，节点编号为 0 到 n - 1 。
#同时给你一个二维整数数组 edges ，其中 edges[i] = [fromi, toi, weighti] ，表示从 fromi 到 toi 有一条边权为 weighti 的 有向 边。
#最后，给你三个 互不相同 的整数 src1 ，src2 和 dest ，表示图中三个不同的点。
#请你从图中选出一个 边权和最小 的子图，使得从 src1 和 src2 出发，在这个子图中，都 可以 到达 dest 。如果这样的子图不存在，请返回 -1 。
#子图 中的点和边都应该属于原图的一部分。子图的边权和定义为它所包含的所有边的权值之和。

import heapq
class Solution(object):
    def minimumWeight(self, n, edges, src1, src2, dest):
        """
        :type n: int
        :type edges: List[List[int]]
        :type src1: int
        :type src2: int
        :type dest: int
        :rtype: int
        """
        g,r = [[] for i in range(n)],[[] for _ in range(n)]
        for f,t,c in edges:
            g[f].append((t,c))
            r[t].append((f,c))
        def sssp(g,s):
            dist = [float('inf')]*n
            st =[(0,s)]
            dist[s] =0
            while st:
                c,f = heapq.heappop(st)
                if c > dist[f]: continue
                for t,c1  in g[f]:
                    if c + c1 < dist[t]:
                        heapq.heappush(st,(c+c1,t))
                        dist[t] = c+c1
            return dist
        a  = sssp(g,src1)
        b = sssp(g,src2)
        c = sssp(r,dest)
        cc =[a[i]+b[i] +c[i] for i in range(n) ]
        ans = min(cc)
        return -1 if ans >= float('inf') else ans