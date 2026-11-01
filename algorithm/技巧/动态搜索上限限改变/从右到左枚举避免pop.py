from collections import Counter, defaultdict, deque

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        pos = defaultdict(list)
        idx_in_pos = [0] * n  # nums[i] 在 pos[nums[i]] 中的下标
        for i, x in enumerate(nums):
            idx_in_pos[i] = len(pos[x])
            pos[x].append(i)

        firsts = []
        first_pos = {}
        ans = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            first_pos[x] = i

            # 把 firsts 中的 x 移到最前面
            j = firsts.index(x) if x in firsts else -1
            if j != 0:  # 优化：j = 0 时无需移动
                if j >= 0:
                    firsts.pop(j)
                firsts.insert(0, x)

            m = len(firsts)
            if m * (m + 1) // 2 > n:  # firsts 不需要这么多元素
                firsts.pop()

            mx, mn = 0, n
            r = i  # 子数组右开端点
            for cnt, x in enumerate(firsts, 1):
                r += cnt
                # [i,r) 必须包含恰好 cnt 个 x
                ps = pos[x]
                k = idx_in_pos[first_pos[x]] + cnt - 1
                if k >= len(ps):  # [i,n) 中的 x 的个数小于 cnt
                    break

                # 更新 mx 和 mn 后，必须满足 mx < r <= mn
                if k < len(ps) - 1:
                    mn = min(mn, ps[k + 1])
                if r > mn:  # 继续遍历，r 更大，mn 更小，无法找到合法子数组
                    break

                mx = max(mx, ps[k])
                if mx < r:
                    ans += 1

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-frequency-staircase-subarrays-ii/solutions/4048447/bao-li-mei-ju-pythonjavacgo-by-endlessch-skjn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。