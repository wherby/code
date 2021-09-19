from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed) :
        n = len(changed)
        changed = sorted(changed,reverse=True)
        dic=defaultdict(int)
        res =[]
        for i in range(n):
            t = changed[i]
            if t not in dic:
                if t %2 ==1:
                    return []
                x= t//2
                dic[x] +=1
                res.append(x)
            else:
                dic[t] -=1
                if dic[t] ==0:
                    del dic[t]
        if len(res) == n//2:
            return res
        else:
            return [] 
            


Solution().findOriginalArray([1,3,4,2,6,8])
