def quickPow(x,y):
    mod = 10**9+7
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ls =[]
        acc =0
        while n >0:
            if n %2 ==1:
                ls.append(acc)
            n = n //2 
            acc+=1
        mod = 10**9+7
        #print(ls)
        m= len(ls)
        pls = [0]*(m+1)
        for i in range(m):
            pls[i+1] = pls[i] + ls[i]
        ret =[]
        for a,b in queries:
            k = pls[b+1] - pls[a]
            ret.append(quickPow(2,k))
        return ret
        
            


re =Solution().productQueries(n = 15, queries = [[0,1],[2,2],[0,3]])
print(re)