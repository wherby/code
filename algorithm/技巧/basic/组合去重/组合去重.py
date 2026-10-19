# https://leetcode.cn/problems/remove-invalid-parentheses
# algorithm/技巧/basic/组合去重/暴力枚举.py
# 这里做不选操作，如何能避免重复路线，这里采用了直接跳过所有重复的数字，对同一值只采取单向选择 只有从选择到不选的选择逻辑，这样就避免了重复

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        target = left = 0
        for ch in s:
            if ch == '(':
                target += 1
                left += 1
            elif ch == ')' and left > 0:
                left -= 1
        target -= left  # 移除多余的 left 个左括号

        n = len(s)
        ans = []
        path = []

        # 当前枚举到 s[i]，已选 left 个左括号和 right 个右括号
        def dfs(i: int, left: int, right: int) -> None:
            # 剪枝（最后一个判断条件是剩余字符个数不足以让我们选出 target*2 个括号）
            if left < right or left > target or left + right + n - i < target * 2:
                return

            if i == n:  # 上面剪枝了，这里一定选了 target 个左右括号
                ans.append(''.join(path))
                return

            ch = s[i]

            # 不选 ch
            if ch == '(' or ch == ')':
                # 后面所有等于 ch 的括号都不选
                # 如果不跳过这些括号，会导致「选 ch 不选 ch'」和「不选 ch 选 ch'」这两种情况都会加到 ans 中，这就重复了
                j = i + 1
                while j < n and s[j] == ch:
                    j += 1
                dfs(j, left, right)

            # 选 ch
            if ch == '(':
                left += 1
            elif ch == ')':
                right += 1
            path.append(ch)
            dfs(i + 1, left, right)
            path.pop()  # 恢复现场

        dfs(0, 0, 0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/remove-invalid-parentheses/solutions/4038185/liang-chong-fang-fa-bfs-hui-su-pythonjav-4hya/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。