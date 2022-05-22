class Solution(object):
    def minimumLines(self, ls):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        ls.sort()
        n = len(ls)
        pre=[10**99,1]
        cnt =0
        for i in range(1,n):
            a1,a2 = ls[i],ls[i-1]
            k = [(a2[1]-a1[1]) ,(a2[0]-a1[0])]
            if k[1]*pre[0] != k[0]*pre[1]:
                cnt +=1
            #print(pre,k)
            pre = k
        return cnt
    
re = Solution().minimumLines([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]])
print(re)