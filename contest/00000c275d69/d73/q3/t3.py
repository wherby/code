class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        g = [[] for _ in range(n)]
        visited =[0]*n
        res = [set() for _ in range(n)]
        ins = [0]*n
        for f,t in edges:
            g[f].append(t)
            ins[t] +=1
        st = []
        for i in range(n):
            if ins[i] == 0:
                st.append(i)
        while st:
            a = st.pop(0)
            visited[a] =1
            for b in g[a]:
                ins[b] -=1
                if ins[b] ==0:
                    st.append(b)
                for c in res[a]:
                    res[b].add(c)
                res[b].add(a)
        res = [sorted(list(a)) for a in res]
        return res

re =Solution().getAncestors(10,[[5,2],[8,7],[7,2],[8,3],[1,6],[9,0]])
print(re)
            
