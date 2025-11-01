# https://leetcode.cn/problems/count-ways-to-choose-coprime-integers-from-rows/description/
from typing import List, Tuple, Optional

MX = 151
divisors = [[] for _ in range(MX)]
for i in range(1,MX):
    for j in range(i,MX,i):
        divisors[j].append(i)

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m,n =len(mat),len(mat[0])
        divisor_cnt = []
        mod =10**9+7
        mx = 0 
        for row in mat:
            row_max= max(row)
            mx = max(mx,row_max)
            cnt = [0]*(row_max +1)
            for x in row:
                for d in divisors[x]:
                    cnt[d] +=1
            divisor_cnt.append(cnt)
        gcd_cnt =[0]*(mx+1)
        for i in range(mx,0,-1):
            res = 1 
            for cnt in divisor_cnt:
                if i >= len(cnt) or cnt[i] ==0:
                    res = 0 
                    break
                res = res *cnt[i] %mod
            for j in range(i,mx+1,i):
                res -= gcd_cnt[j]
            gcd_cnt[i] = res%mod
        return gcd_cnt[1]%mod

re =Solution().countCoprime([[1,2],[3,4]])
print(re)