# 求恰好等于 改成求大于等于，再求大于等于 k+1 的差值
from collections import defaultdict,deque
class Solution:
    def countSubarrays(self, nums, k: int, m: int) -> int:
        def calc(distinct_limit: int) -> int:
            cnt = defaultdict(int)
            ge_m = 0  # 窗口中的出现次数 >= m 的元素个数
            ans = left = 0
            for x in nums:
                # 1. 入
                cnt[x] += 1
                if cnt[x] == m:
                    ge_m += 1

                # 2. 出
                while len(cnt) >= distinct_limit and ge_m >= k:
                    out = nums[left]
                    if cnt[out] == m:
                        ge_m -= 1
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out]
                    left += 1

                # 3. 更新答案
                ans += left
            return ans

        return calc(k) - calc(k + 1)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-subarrays-with-k-distinct-integers/solutions/3910806/qia-hao-xing-hua-dong-chuang-kou-pythonj-5mll/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。