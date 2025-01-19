from typing import List, Tuple, Optional

# 预处理阶乘以及其逆元
max_n = int(1e5)
fac = [1] * (max_n+1)
facinv = [1] * (max_n+1)

MAX_NUM = int(1e9+7)
for i in range(1,max_n+1):
    fac[i] = fac[i-1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i],MAX_NUM-2,MAX_NUM)


def myComb(n,m):    
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n-m] % MAX_NUM

# 两距离组合
def C(m,n):
    return myComb(m+n,n)
    

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        acc = 0
        def getK(k):
            return (k+1)*k//2
        for i in range(m):
            for j in range(n):
                acc += n*(getK(i)+ getK(m-1-i))
                acc += m*(getK(j) + getK(n-1-j)) 
        acc =acc *myComb(m*n-2,k-2)*facinv[2]%MAX_NUM
        return acc





re =Solution().distanceSum(2,2,2)
print(re)