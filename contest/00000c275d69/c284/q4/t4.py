
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
        g =[[] for _ in range(n)]
        dic={}
        for f,t,cost in edges:
            g[f].append(t)
            dic[(f,t)] = cost
        def dfs(f, des,cost):
            #print(f,des,cost)
            visited[f] =1
            if f == des:
                #print("aaa",cost)
                return cost
            st =[]
            for a in g[f]:
                heapq.heappush(st,(cost + dic[(f,a)],a))
            while st:
                cost,a = heapq.heappop(st)
                if visited[a] : continue
                t = dic[(f,a)]
                dic[(f,a)] =0
                ret = dfs(a,des,cost)
                if ret ==-1:
                    dic[(f,a)] = t
                else:
                    return ret
            return -1
        visited= [0]*n
        a1 = dfs(src2,dest,0)
        print(dic,a1)
        if a1 >0:
            visited = [0]*n
            a2 = dfs(src1,dest,0)
        print(a2)
        return a1
        
re =Solution().minimumWeight(8,[[4,7,24],[1,3,30],[4,0,31],[1,2,31],[1,5,18],[1,6,19],[4,6,25],[5,6,32],[0,6,50]],4,1,6)
print(re)