# https://leetcode.cn/contest/zj-future2022/problems/NBCXIp/
# https://leetcode.cn/contest/zj-future2022/ranking/1/
class Solution:
    def minTransfers(self, a) -> int:
        n = 12
        b = [0 for i in range(n)]
        for x, y, z in a:
            b[x] -= z
            b[y] += z
        f = [0 for i in range(1 << n)]
        for i in range(1 << n):
            s = 0
            for j in range(n):
                if i >> j & 1:
                    s += b[j]
            if s == 0:
                f[i] = 1
        f[0] = 0
        for i in range(1 << n):
            j = i
            while j > 0:
                f[i] = max(f[i], f[j] + f[i - j])
                j = (j - 1) & i
        return 12 - f[(1 << n) - 1]