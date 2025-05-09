
MOD = 1_000_000_007
MX = 41

fac = [0] * MX  # f[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cnt = [0] * 10
        total = 0
        for c in map(int, num):
            cnt[c] += 1
            total += c

        if total % 2:
            return 0

        n = len(num)
        n1 = n // 2
        f = [[0] * (total // 2 + 1) for _ in range(n1 + 1)]
        f[0][0] = 1
        sc = s = 0
        for i, c in enumerate(cnt):
            sc += c
            s += c * i
            # 保证 left2 <= n-n1，即 left1 >= sc-(n-n1)
            for left1 in range(min(sc, n1), max(sc - (n - n1) - 1, -1), -1):   # cnt 循环
                left2 = sc - left1
                # 保证分给第二个集合的元素和 <= total/2，即 left_s >= s-total/2
                for left_s in range(min(s, total // 2), max(s - total // 2 - 1, -1), -1): # sum 循环
                    res = 0
                    for k in range(max(c - left2, 0), min(c, left1) + 1):  # k是受 cnt和sum 限制的
                        if k * i > left_s:
                            break
                        res += f[left1 - k][left_s - k * i] * inv_f[k] * inv_f[c - k]
                    f[left1][left_s] = res % MOD
        return fac[n1] * fac[n - n1] * f[n1][total // 2] % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-number-of-balanced-permutations/solutions/2975507/duo-zhong-ji-pai-lie-shu-ji-shu-dppython-42ky/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re =Solution().countBalancedPermutations("409871932342390718772")
print(re)