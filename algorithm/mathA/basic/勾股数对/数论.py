
from math import isqrt

MX = isqrt(500) + 1

# 预处理莫比乌斯函数
# 当 n > 1 时，sum_{d|n} mu[d] = 0
# 所以 mu[n] = -sum_{d|n ∧ d<n} mu[d]
mu = [0] * MX
mu[1] = 1
for i in range(1, MX):
    for j in range(i * 2, MX, i):
        mu[j] -= mu[i]  # i 是 j 的真因子

# 预处理不含平方因子的因子列表，用于 count_coprime
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    if mu[i]:
        for j in range(i, MX, i):
            divisors[j].append(i)  # i 是 j 的因子，且 mu[i] != 0

# 返回 [1,n] 中与 x 互质的整数个数
def count_coprime(n: int, x: int) -> int:
    return sum(mu[d] * (n // d) for d in divisors[x])

# 返回 [1,n] 中与奇数 x 互质的奇数个数
# 与 x 互质的整数个数 - 与 x 互质的偶数个数
def count_coprime_odd(n: int, x: int) -> int:
    return count_coprime(n, x) - count_coprime(n // 2, x)

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        u = 3
        while u * u < n * 2:
            l = 1
            while l < u and u * u + l * l <= n * 2:
                num = (n * 2) // (u * u + l * l)
                # 对于 [l,r] 中的整数 v，2n // (u^2 + v^2) 都等于 num
                r = min(isqrt(n * 2 // num - u * u), u - 1)  # 推导过程见题解
                # 只有与 u 互质的奇数 v 才能得到本原勾股数组
                num_coprime_odd_v = count_coprime_odd(r, u) - count_coprime_odd(l - 1, u)
                ans += num * num_coprime_odd_v
                l = r + 1
            u += 2
        return ans * 2  # (a,b,c) 和 (b,a,c) 各算一次

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-square-sum-triples/solutions/869409/go-yu-chu-li-you-hua-by-endlesscheng-61mj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。