# dp[i][j] 表示第i个数字的时候有j个逆序对，(i,j)状态只能由(i-1，j-k) k<=i 的状态转移过来
# https://leetcode.cn/problems/count-the-number-of-inversions/solutions/2953751/python3javacgotypescript-yi-ti-yi-jie-do-73li/?envType=daily-question&envId=2024-10-17

from typing import List, Tuple, Optional
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10**9+7
        rd ={}
        requirements.sort()
        for a,b in requirements:
            rd[a] = b 
        mx = requirements[-1][1]
        dp=[[0]*(mx+1) for _ in range(n)]
        
        if 0 in rd and rd[0] != 0:
            return 0
        dp[0][0]=1 # 初始条件
        for i in range(1,n):
            acc = 0
            for j in range(mx+1):
                acc += dp[i-1][j]
                if j>i:
                    acc -= dp[i-1][j-i-1]
                dp[i][j] = acc 
            if i in rd:
                for j in range(mx+1):
                    if j != rd[i]:
                        dp[i][j] =0
        #print(dp)
        return dp[-1][requirements[-1][1]] %mod 
    
re =Solution().numberOfPermutations(n = 3, requirements = [[2,2],[0,1]])
print(re)


        
