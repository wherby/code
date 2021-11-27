from bisect import bisect_left
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        n = len(toppingCosts)
        ls =[0]* 20002
        res = [0]
        for i in range(n):
            tp =[]
            a1 = toppingCosts[i]
            for r in res:
                tp.append(r+a1)
                tp.append(r + a1*2)
            res = list(set(res +tp))
        
        keys = res
        #print(keys[:100])
        for b in baseCosts:
            for k in keys:
                if b+k <= 20000:
                    ls[b+k] =1
        lsa =[]
        for i in range(20001):
            if ls[i] ==1:
                lsa.append(i) 
        lsa.append(100000000000)
        idx = bisect_left(lsa,target)
        #print(lsa[:100])
        #print(lsa)
        if lsa[idx] == target:
            return target
        if idx ==0:
            return lsa[0]
        if  lsa[idx] -target >= target- lsa[idx-1]:
            return lsa[idx-1]
        
        return lsa[idx]

re = Solution().closestCost(baseCosts = [9,10,1], toppingCosts = [1,8,8,1,1,8], target = 8)
print(re)
        

                
        
            