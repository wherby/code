from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        g = defaultdict(list)
        for a,b in richer:
            g[b].append(a)
        n = len(quiet)
        res =[i for i in range(n)]
        mem =[-1]*n
        def dfs(i):
            if mem[i] != -1 : return mem[i]
            minV = quiet[i]
            minP = i
            for x in g[i]:
                tv,tp = dfs(x)
                if tv < minV:
                    minV = tv
                    minP = tp
            mem[i] = (minV,minP)
            return (minV,minP)
        for i in range(n):
            dfs(i)
            res[i] = mem[i][1]
        #print(mem)
        return res            
        



re = Solution().loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0])
print(re)