

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        num_pos = [[] for _ in range(k)]  # 2*nums[i] % k 出现的所有位置
        first_pos = [-1] * k  # 前缀和 % k 首次出现的位置
        last_pos = [-1] * k  # 前缀和 % k 最后一次出现的位置
        first_pos[0] = last_pos[0] = 0
        s = 0  # 前缀和
        ans = 0

        for i, x in enumerate(nums):
            num_pos[x * 2 % k].append(i)
            s = (s + x) % k
            r = i + 1
            l = first_pos[s]
            if l < 0:
                first_pos[s] = r
            else:
                # 不取反时的最大长度
                ans = max(ans, r - l)
            last_pos[s] = r

        # 枚举 s[l]%k 和 s[r]%k，判断是否存在满足要求的 i
        for sl, l in enumerate(first_pos):
            if l < 0:
                continue
            for sr, r in enumerate(last_pos):
                if r - l <= ans:  # 最优性优化：ans 无法增大
                    continue
                # 2*nums[i]%k = (sr-sl)%k
                pos = num_pos[(sr - sl) % k]
                idx = bisect_left(pos, l)
                if idx < len(pos) and pos[idx] < r:
                    ans = r - l

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/solutions/4035243/mei-ju-qian-zhui-he-pythonjavacgo-by-end-nlum/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。