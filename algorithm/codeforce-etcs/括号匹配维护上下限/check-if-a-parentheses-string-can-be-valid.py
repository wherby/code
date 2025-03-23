# 可变括号匹配，维护上下限

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        mn = mx = 0
        for b, lock in zip(s, locked):
            if lock == '1':  # 不能改
                d = 1 if b == '(' else -1
                mx += d
                if mx < 0:  # c 不能为负
                    return False
                mn += d
            else:  # 可以改
                mx += 1  # 改成左括号，c 加一
                mn -= 1  # 改成右括号，c 减一
            if mn < 0:  # c 不能为负
                mn = 1  # 此时 c 的取值范围都是奇数，最小的奇数是 1
        return mn == 0  # 说明最终 c 能是 0

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/check-if-a-parentheses-string-can-be-valid/solutions/1178043/zheng-fan-liang-ci-bian-li-by-endlessche-z8ac/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。