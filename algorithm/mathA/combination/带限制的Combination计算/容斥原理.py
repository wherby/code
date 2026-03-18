# dp(i,j,k)表示当前剩余i个0，j个1，k表示最后一个数字为0还是1，满足条件的数组数量
# (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - (dfs(i - limit - 1, j, 1) if i > limit else 0)) % MOD  为什么是减去的是dfs(i - limit - 1, j, 1)，这个数字表示了刚刚好有limit+1个0的情况，这个情况的最后一个数字是1，然后limit+1个0


from functools import cache
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if k == 0:
                return (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - (dfs(i - limit - 1, j, 1) if i > limit else 0)) % MOD
            else:  # else 可以去掉，这里仅仅是为了代码对齐
                return (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - (dfs(i, j - limit - 1, 0) if j > limit else 0)) % MOD
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        dfs.cache_clear()  # 防止爆内存
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/solutions/2758868/dong-tai-gui-hua-cong-ji-yi-hua-sou-suo-37jdi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。