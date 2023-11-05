from collections import defaultdict
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        n = len(favoriteCompanies)
        fas = []
        for fa in favoriteCompanies:
            tp = set(fa)
            fas.append(tp)
        ls =[0]*n
        for i in range(n):
            di = fas[i]
            for j in range(n):
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