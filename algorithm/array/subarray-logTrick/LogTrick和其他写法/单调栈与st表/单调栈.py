from bisect import bisect_right, insort_left, bisect_left


class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        data = []
        st = []
        ans = 0

        for i, x in enumerate(nums):
            # x 入单调栈
            while st and nums[st[-1]] >= x:
                st.pop()
            st.append(i)

            # 计算右端点为 i 的子数组与值
            for p in data:
                p[0] &= x
            # x 单独一个数作为子数组
            data.append([x, i])

            # 原地去重（相同与值只保留最左边的）
            idx = 1
            for j in range(1, len(data)):
                if data[j][0] != data[j - 1][0]:
                    data[idx] = data[j]
                    idx += 1
            del data[idx:]

            for k, (and_val, left) in enumerate(data):
                # 判断子数组最小值是否为 and_val
                j = bisect_left(st, and_val, key=lambda j: nums[j])
                if j == len(st) or nums[st[j]] != and_val:
                    continue

                right = data[k + 1][1] - 1 if k < len(data) - 1 else i
                right = min(right, st[j])
                # 注：由于 nums[st[j-1]] < and_val，假如子数组包含 st[j-1]，那么与值会比 and_val 还小，矛盾
                # 所以子数组不可能包含 st[j-1]，所以无需考虑 st[j-1]
                ans += max(right - left + 1, 0)

        return ans


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-consistent-subarrays-ii/solutions/4057247/logtrick-dan-diao-zhan-pythonjavacgo-by-m1zrb/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
