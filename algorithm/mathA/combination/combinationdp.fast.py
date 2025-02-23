# mod 是质数
MOD = 1_000_000_007
MX = 100_001  # 根据题目数据范围修改

fac = [0] * MX  # fac[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

# 从 n 个数中选 m 个数的方案数
def comb(n: int, m: int) -> int:
    return fac[n] * inv_f[m] * inv_f[n - m] % MOD if 0 <= m <= n else 0

# class Solution:
#     def solve(self, nums: List[int]) -> int:
#         # 预处理的逻辑写在 class 外面，这样只会初始化一次

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/mDfnkW/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(comb(10**5,50000))