from collections import defaultdict
class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        dic2= defaultdict(list)
        
        n = len(pairs)
        for a,b in pairs:
            if a not in dic:
                dic[a] = [0,0]
            if b not in dic:
                dic[b] = [0,0]
            dic[a][0] +=1
            dic[b][1] +=1
        #print(dic)
        for i,p in enumerate(pairs):
            dic2[p[0]].append(p[1])

        cand = []
        for k,v in dic.items():
            if v[0]>v[1]:
                cand.append(k)
        #用dfs会有合并和递归数目限制问题
        def dfs(start,res):
            if len(dic2[start]) ==0:
                return
            k =dic2[start].pop()
            tmp=[]
            tmp.append([start,k])
            dfs(k,tmp)
            while len(dic2[start]):
                k = dic2[start].pop()
                anotherCircle = [[start,k]]
                anotherCircle=dfs(k,anotherCircle)
                res.extend(anotherCircle)
            res.extend(tmp)
            return res
            
            
        res =[]
        if len(cand) ==0:
            dfs(pairs[0][0],res)
        else:
            for c in cand:
                dfs(c,res)
        return res

pairs = [[1,3],[3,2],[2,1]]
pairs= [[1,2],[1,3],[2,1]]
#pairs =[[8,5],[8,7],[0,8],[0,5],[7,0],[5,0],[0,7],[8,0],[7,8]]
re= Solution().validArrangement(pairs )
print(re)
        