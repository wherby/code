# https://leetcode.cn/problems/05ZEDJ/

class Solution(object):
    def volunteerDeployment(self, finalCnt, totalNum, edges, plans):
        """
        :type finalCnt: List[int]
        :type totalNum: int
        :type edges: List[List[int]]
        :type plans: List[List[int]]
        :rtype: List[int]
        """
        n = len(finalCnt)
        g = [[] for _ in range(n+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ls = [0]*(n+1)
        ls2 =[0]*(n+1)
        for i,a in enumerate(finalCnt):
            ls[i+1] = a 
        ls2[0] = 1 
        #print(ls,ls2)
        for op,i in plans[::-1]:
            if op==1:
                ls[i] = ls[i]*2
                ls2[i] = ls2[i]*2
            if op == 2:
                for b in g[i]:
                    ls[b] -= ls[i]
                    ls2[b] -= ls2[i]
            if op ==3:
                for b in g[i]:
                    ls[b] += ls[i]
                    ls2[b] += ls2[i]
            #print(op,i,ls,ls2)
        x= (totalNum - sum(ls)) //(sum(ls2))
        ret = [0]*(n+1)
        for i in range(n+1):
            ret[i] = ls[i] + ls2[i]*x 
        return ret


#re = Solution().volunteerDeployment(finalCnt = [4,13,4,3,8], totalNum = 54, edges = [[0,3],[1,3],[4,3],[2,3],[2,5]], plans = [[1,1],[3,3],[2,5],[1,0]])
re = Solution().volunteerDeployment(finalCnt = [1,16], totalNum = 21, edges = [[0,1],[1,2]], plans = [[2,1],[1,0],[3,0]])
print(re)