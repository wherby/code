from typing import List, Tuple, Optional

mod = 10**9+7
MX =1001
s = [[0]*MX for _ in range(MX)]
s[0][0] =1 

for i in range(1,MX):
    for j in range(1,MX):
        s[i][j] = (s[i-1][j-1] + j * s[i-1][j]) % mod 

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        ans = 0 
        pre = pow_y =1
        for i in range(1, min(n,x) +1):
            pre= pre*(x+1-i) %mod 
            pow_y = pow_y* y %mod 
            ans += pre *s[n][i] * pow_y
        return ans %mod

re =Solution().numberOfWays(n = 3, x = 3, y = 4)
print(re)