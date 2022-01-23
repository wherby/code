from collections import defaultdict
class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        g=[[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                a = statements[i][j]
                if a ==2: continue
                if a ==1: g[i].append([j,2])
                if a ==0: g[i].append([j,1])
        mx =0
        #print(g)
        def verify(state):
            #print(state)
            cand =[]
            dic = defaultdict(int)
            for i in range(n):
                if state & (1<<i):
                    cand.append(i)
                    dic[i] =2
                else:
                    dic[i] =1
            for c in cand:
                for i,s in g[c]:
                    if dic[i] ==0 or dic[i] == s:
                        dic[i] =s
                    else:
                        return 0
            return len(cand)
        for s in range(1<<n):
            mx = max(mx,verify(s))
        return mx

re = Solution().maximumGood(statements = [[2,0],[0,2]])
print(re)