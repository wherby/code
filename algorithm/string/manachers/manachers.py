#https://leetcode.com/problems/palindrome-partitioning-ii/submissions/
class Solution:
    def minCut(self, s: str) -> int:
        def manachers(S):
            A = "@#" + "#".join(S) + "#$"
            Z = [0] * len(A)
            center = right =0
            for i in range(1,len(A)-1):
                if i < right:
                    Z[i] = min(right -i,Z[2*center -i]) # Z[2*center -i]是 i 关于center的对称点， 因为在[left, right]上对称，则 对称点的对称性是对称的
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
        #print(dp)
        return dp[-2]
        


s="ccaaaccabacb"
re = Solution().minCut(s)
print(re)