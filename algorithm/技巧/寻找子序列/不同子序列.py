# https://leetcode.cn/problems/distinct-subsequences/description/
from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if i < j:
                return 0
            if j < 0:
                return 1
            res = dfs(i - 1, j)  # 删除 s[i]
            if s[i] == t[j]:
                res += dfs(i - 1, j - 1)  # 不删 s[i]，和 t[j] 匹配
            return res
        return dfs(len(s) - 1, len(t) - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/distinct-subsequences/solutions/3060706/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-9va6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

re = Solution().numDistinct(s = "babgbag", t = "bag")
print(re)