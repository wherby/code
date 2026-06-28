# https://leetcode.cn/problems/count-subarrays-with-majority-element-ii/solutions/3826966/mei-ju-you-wei-hu-zuo-on-zuo-fa-pythonja-ojfh/

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1  # 为什么加个 0？见 525 题我的题解
        ans = s = f = 0
        for x in nums:
            if x == target:
                f += cnt[s]
                s += 1
            else:
                s -= 1
                f -= cnt[s]
            ans += f
            cnt[s] += 1
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-subarrays-with-majority-element-ii/solutions/3826966/mei-ju-you-wei-hu-zuo-on-zuo-fa-pythonja-ojfh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。