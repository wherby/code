from typing import List, Tuple, Optional

MOD = 1_000_000_007

# 预处理组合数
c = [[0] * 14 for _ in range(10013)]
c[0][0] = 1
for i in range(1, 10013):
    c[i][0] = 1
    for j in range(1, 14):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        ans = []
        for n, k in queries:
            res = 1
            i = 2
            while i * i <= k:
                if k % i == 0:  # i 是 k 的质因子
                    e = 0
                    while k % i == 0:
                        e += 1  # 统计有多少个质因子 i
                        k //= i
                    res = res * c[e + n - 1][e] % MOD
                i += 1
            if k > 1:  # 还剩下一个质因子
                res = res * n % MOD
            ans.append(res)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-ways-to-make-array-with-product/solutions/2713481/tu-jie-zhi-yin-zi-fen-jie-fang-qiu-wen-t-fboo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。