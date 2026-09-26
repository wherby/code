# 利用hash值，把值域映射到更大的值域，当使用 64 位（64-bit）的随机整数时，$10^5$ 个数字发生至少一次哈希冲突的概率极其微小，约为 $2.7 \times 10^{-10}$（即十亿分之 0.27）。
# 而不同的数字xor 为0 的概率为 1/(2**64)
# 然后利用双指针计算k个区域的左端点位置

from collections import defaultdict,deque
import random
class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        s = [0] * (n + 1)
        # 把 nums[i] 映射成一个随机的 uint64
        mp = defaultdict(lambda: random.getrandbits(64))  # 或者 randrange(1 << 64)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] ^ mp[x]

        def calc_left(k: int) -> list[int]:
            lefts = [0] * n
            cnt = defaultdict(int)
            l = 0
            for i, x in enumerate(nums):
                cnt[x] += 1
                while len(cnt) >= k:
                    v = nums[l]
                    if cnt[v] > 1:
                        cnt[v] -= 1
                    else:
                        del cnt[v]  # 保证 len(cnt) 是窗口内的不同元素个数
                    l += 1
                lefts[i] = l
            return lefts

        l1 = calc_left(k + 1)
        l2 = calc_left(k)

        return [s[r + 1] == s[l] and l1[r] <= l < l2[r] for l, r in queries]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/valid-k-unique-subarrays-i/solutions/4016355/yi-huo-ha-xi-chi-xian-shu-zhuang-shu-zu-pkxwi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。