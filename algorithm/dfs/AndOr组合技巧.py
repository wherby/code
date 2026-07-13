# 使用 and 组合各个条件，避免了if 判定 
from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> bool:
            if i < 0 and j < 0:
                return True
            return i >= 0 and s1[i] == s3[i + j + 1] and dfs(i - 1, j) or \
                   j >= 0 and s2[j] == s3[i + j + 1] and dfs(i, j - 1)

        return dfs(n - 1, m - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/interleaving-string/solutions/3060419/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-qcen/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。