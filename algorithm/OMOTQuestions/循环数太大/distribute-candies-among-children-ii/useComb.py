

def c2(n: int) -> int:
    return n * (n - 1) // 2 if n > 1 else 0

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/distribute-candies-among-children-ii/solutions/2522969/o1-rong-chi-yuan-li-pythonjavacgo-by-end-2woj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。