class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i])
                while A[i + Z[i]+1] == A[i-Z[i]-1]:
                    Z[i] +=1
                if i + Z[i] > right:
                    center,right = i , i+ Z[i]
            return Z[2:-2:1]
    
        re= manachers(s)
        print(re)
        
        dp=[i-1 for i in range(len(s)+2)]
        for j in range(len(re)):
            t = re[j]
            while t >0:
                xp =j//2 +t//2 +1
                
                dp[xp] = min(dp[xp],dp[xp -t]+1)
                #print(t,xp,j,xp-t,dp[xp])
                t= t-2
        print(dp)
        k=dp[-2]
        if k ==2 or k ==0:
            return True
        return False

s = "bbab"
re = Solution().checkPartitioning(s)
print(re)