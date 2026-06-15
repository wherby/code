# https://leetcode.cn/problems/maximum-score-with-co-prime-element/

from typing import List, Tuple, Optional


def prepare(M):
    # 初始化数组
    mu = [1] * M  # 莫比乌斯函数
    F = [0] * M   # 最小质因子
    q = []        # 存储质数
    
    mu[1] = 1     # 规定mu[1] = 1
    
    for i in range(2, M):
        if not F[i]:  # i是质数
            F[i] = i
            q.append(i)
            mu[i] = -1  # 质数的mu值为-1
        
        # 用当前已筛出的质数q[j]去标记合数i*q[j]
        for p in q:
            if i * p >= M:
                break
            F[i * p] = p  # 合数i*p的最小质因子是p
            if i % p == 0:
                mu[i * p] = 0  # i*p包含平方因子p^2
                break
            else:
                mu[i * p] = -mu[i]  # 根据mu的定义更新
    
    return mu, F, q

# 示例调用
M = 10**5+1  
mu, F, primes = prepare(M)

class Solution:
    def maxScore(self, nums: List[int], maxVal: int) -> int:
        mx = max(max(nums),maxVal) +1 
        cnt = [0]*mx 
        for a in nums:
            cnt[a] +=1
        divs = [[] for i in range(mx)]
        dp = [0]*mx
        for i in range(2,mx):
            acc = 0 
            for j in range(i,mx,i):
                divs[j].append(i)
                acc +=cnt[j]
            dp[i] = acc
        ret =1 if cnt[1] else 0 

        for i in range(2,mx):
            acc = 0 
            for b in divs[i]:
                acc -= dp[b]*mu[b]
                #print(dp[b],mu[b],b)
            if i <=maxVal:
                if cnt[i]:
                    ret = max(ret,i- (acc-1))
                elif acc>0:
                    ret = max(ret,i-acc)
                else:
                    ret =max(ret,i-1)
            else:
                if cnt[i]:
                    ret = max(ret, i-(acc-1))
            #print(ret,i,acc,divs[i])
        return ret

re = Solution().maxScore(nums = [42], maxVal = 312)
#re = Solution().maxScore(nums = [3,4,6], maxVal = 5)
print(re)