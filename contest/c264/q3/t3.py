from collections import defaultdict
class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        n  = len(parents)
        g= [[] for i in range(n)]
        for i in range(n):
            t = parents[i]
            if t == -1 :
                continue
            g[t].append(i)
            #print(g,t,i)
        ls = [[] for i in range(n)]
        #print(g)
        def dfs(a):
            #print(a)
            if len(g[a]) ==0:
                return 0
            sm = 0
            for i in g[a]:
                #print(i)
                #t1= i
                t1 = dfs(i)
                #print(i,t1)

                ls[a].append(t1+1)
                sm += t1 +1
            #ls[a].append(sm)
            return sm
        dfs(0)
        mx= 0
        dic=defaultdict(int)
        for item in ls:
            if len(item) == 0:
                mx = max(mx, n-1)
                dic[n-1] +=1
            else:
                res = n - sum(item)-1
                
                if res >0:
                    for t1 in item:
                        res *=t1
                    mx = max(mx,res)
                    dic[res]+=1
                else:
                    res =1
                    for t1 in item:
                        res *=t1
                    mx = max(mx,res)
                    dic[res]+=1
        return dic[mx]

parents = [-1,2,0,2,0]
mx=Solution().countHighestScoreNodes(parents)
print(mx)