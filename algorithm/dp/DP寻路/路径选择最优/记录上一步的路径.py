from bisect import bisect_right,insort_left,bisect_left
from math import inf

MX = 1001
is_prime = [True] * MX
primes = []
for i in range(2, MX):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MX, i):
            is_prime[j] = False  # j 是质数 i 的倍数

class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        m = bisect_right(primes, n)

        f = [[inf] * (s + 1) for _ in range(m + 1)]
        f[m][0] = 0

        # 倒着 DP，这样可以正序输出方案，且保证越靠前的质数越小
        for i in range(m - 1, -1, -1):
            x = primes[i]
            for j in range(s + 1):
                if j < x:
                    f[i][j] = f[i + 1][j]
                else:
                    f[i][j] = min(f[i + 1][j], f[i + 1][j - x] + 1)

        j = s
        while j > 0 and f[0][j] == inf:
            j -= 1

        ans = []
        for i in range(m):
            if j == 0:
                break
            x = primes[i]
            # 靠前的质数越小越好，f[i+1][j-x]+1 = f[i+1][j] 的时候要选
            if f[i + 1][j - x] + 1 <= f[i + 1][j]:
                ans.append(x)
                j -= x

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/prime-subset-selection-ii/solutions/4041612/0-1-bei-bao-shu-chu-ju-ti-fang-an-python-x6g1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。