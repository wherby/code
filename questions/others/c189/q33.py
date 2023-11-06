from collections import defaultdict
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        n = len(favoriteCompanies)
        fas = []
        for fa in favoriteCompanies:
            tp = set(fa)
            fas.append(tp)
        dic =defaultdict(list)
        for i,ls in enumerate(favoriteCompanies):
            for a in ls:
                dic[a].append(i)
        res =[]
        ls =[0]*n
        for i in range(n):
            di = fas[i]
            vaaa = favoriteCompanies[i][0]
            for j in dic[vaaa]:
                if i ==j :
                    continue
                dj = fas[j]
                isContaine =True
                for k in di:
                    if k not in dj:
                        isContaine =False
                        break
                if isContaine == True:
                    ls[i] +=1
        res =[]
        for i in range(n):
            if ls[i] ==0:
                res.append(i)
        return res
    

favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]

re =Solution().peopleIndexes(favoriteCompanies)
print(re)          

a= [[1,2],[3,4]]
for x,y in a:
    print(x,y)