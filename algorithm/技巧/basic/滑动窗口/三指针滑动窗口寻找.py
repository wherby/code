# https://leetcode.cn/problems/valid-subarrays-with-matching-sum-digits-i/description/



from itertools import accumulate

class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        pre = list(accumulate(nums, initial=0))
        ans = 0

        # 枚举子数组和的十进制长度
        low, high = x, x + 1
        while low <= pre[-1]:
            # 计算子数组和在 [low, high-1] 中，且子数组和模 10 为 x 的子数组个数
            cnt = [0] * 10
            left1 = left2 = 0
            for s in pre:
                # 随着 s 的增大，<= s-high 的前缀和离开窗口，<= s-low 的前缀和进入窗口
                while pre[left1] <= s - high:
                    cnt[pre[left1] % 10] -= 1
                    left1 += 1
                while pre[left2] <= s - low:
                    cnt[pre[left2] % 10] += 1
                    left2 += 1
                ans += cnt[(s - x) % 10]
            low *= 10
            high *= 10

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/valid-subarrays-with-matching-sum-digits-i/solutions/3986177/onlogs-zuo-fa-qian-zhui-he-hua-dong-chua-y1o3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。