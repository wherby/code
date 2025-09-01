# https://leetcode.cn/problems/sorted-gcd-pair-queries/
# https://leetcode.cn/problems/sorted-gcd-pair-queries/solutions/2940431/jing-dian-shu-lun-jie-fa-onulogufu-za-du-tgr6/
# 利用莫比乌斯反演， 因为倍数容斥是需要从大到小依次计算
# 而莫比乌斯函数，则可以通过最终的二项式展开得到的符号，直接计算，求cnt2的时候，每个值与前后无关，可以[并行化]处理
from typing import List, Tuple, Optional
from itertools import accumulate
from bisect import bisect_right,insort_left,bisect_left

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
M = 50000+1  # 假设上限为20
mu, F, primes = prepare(M)

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        cnt = [0] * (max_val+1) 
        for x in nums:
            cnt[x] += 1
        cnt2 = [0]*(max_val+1)
        for i in range(1,max_val+1 ):
            cnt2[i] -= cnt[i] # 因为pair数目是 c*(c-1)， 所以先减去c? 
            for j in range(2*i,max_val+1,i):
                cnt[i] += cnt[j]
        for i in range(1,max_val+1):
            for j in range(1,max_val//i+1):
                cnt2[i] += mu[j] * cnt[i*j]*cnt[i*j]
            cnt2[i] = cnt2[i]//2 + cnt2[i-1]
        ans = []
        for q in queries:
            ans.append(bisect_right(cnt2,q))
        return ans

ls = [2,3,4,6,8,12]
re =Solution().gcdValues(ls,[3,5,7,9])
print(re)
