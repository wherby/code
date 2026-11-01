


class Solution:
    # 模板来源：https://leetcode.cn/discuss/post/3580371/fen-xiang-gun-ti-dan-wei-yun-suan-ji-chu-nth4/
    def log_trick(self, nums: list[int]) -> list[list[int]]:
        res = [[0] * 26 for _ in nums]
        or_left = []  # (子数组或值，最小左端点)

        for i, x in enumerate(nums):
            # 计算右端点为 i 的子数组或值
            for p in or_left:
                p[0] |= x
            # x 单独一个数作为子数组
            or_left.append([x, i])

            # 原地去重（相同或值只保留最左边的）
            idx = 1
            for j in range(1, len(or_left)):
                if or_left[j][0] != or_left[j - 1][0]:
                    or_left[idx] = or_left[j]
                    idx += 1
            del or_left[idx:]

            for k, (_, left) in enumerate(or_left):
                right = or_left[k + 1][1] - 1 if k < len(or_left) - 1 else i
                # 对于左端点在 [left, right]，右端点为 i 的子数组，OR 值都相同
                res[i][len(or_left) - 1 - k] = right - left + 1

        return res

    def countMagicalPairs(self, s: str) -> int:
        a = [1 << (ord(ch) - ord('a')) for ch in s]
        pre = self.log_trick(a)
        a.reverse()
        suf = self.log_trick(a)  # 相当于倒着遍历 a
        suf.reverse()

        ans = 0
        for i in range(len(pre) - 1):
            for p, s in zip(pre[i], suf[i + 1]):
                if p == 0 or s == 0:
                    break
                ans += p * s
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-magical-substring-pairs-ii/solutions/4048362/liang-chong-fang-fa-qia-hao-xing-hua-don-61cn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。