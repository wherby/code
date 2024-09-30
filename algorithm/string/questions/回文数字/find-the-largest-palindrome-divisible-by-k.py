
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        pow10 = [1]*n 
        for i in range(1,n):
            pow10[i] = pow10[i-1]*10 %k 
        
        ans = [None] *n 

        m = (n+1)//2 
        vis =[[False] *k for _ in range(m+1)]

        def dfs(i,j):
            if i == m:
                return j == 0 
            vis[i][j] = True
            for d in range(9,-1,-1):
                if n %2 and i == m-1:
                    j2 = (j+ d*pow10[i]) %k 
                else:
                    j2 = (j + d*(pow10[i] + pow10[-1-i])) % k 
                if not vis[i+1][j2] and dfs(i+1,j2):
                    ans[i] = ans[-i-1] = str(d)
                    return True
            return False
        dfs(0,0)
        return "".join(ans)
    
re =Solution().largestPalindrome(14,8)
print(re)