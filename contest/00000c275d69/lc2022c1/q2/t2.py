class Solution(object):
    def perfectMenu(self, materials, cookbooks, attribute, limit):
        """
        :type materials: List[int]
        :type cookbooks: List[List[int]]
        :type attribute: List[List[int]]
        :type limit: int
        :rtype: int
        """
        n = len(cookbooks)
        dp = [[0]*(limit +2) for _ in range(n+1)]
        m = len(cookbooks[0])
        
        def verifyState(state):
            acc = [0]*m
            good,full =0,0
            for i in range(n):
                if state & (1<<i):
                    #print(state,1<<i,state & (1<<i))
                    bk = cookbooks[i]
                    for j in range(m):
                        acc[j] += bk[j]
                    good+= attribute[i][0]
                    full += attribute[i][1]
                        #print(j,good,full)
            isGood = True
            for i in range(m):
                if acc[i] > materials[i]:
                    isGood = False
                    good =-1
                    full =-1
            return (good,full)
        
        mx = -1
        for i in range(1<<n):
            good,full = verifyState(i)
            #print(i,good,full)
            if full >=limit:
                mx = max(mx,good)
        return mx
    
re =Solution().perfectMenu( [3,2,4,1,2], [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]], [[3,2],[2,4],[7,6]], 5)
print(re)