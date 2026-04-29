# 12.5s 线段树

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        class SegmentTree:
            def __init__(self, size):
                self.n = 1
                while self.n < size:
                    self.n <<= 1
                self.tree = [0] * (2 * self.n)
            
            def update(self, pos, value):
                # pos 是 1-based
                pos += self.n - 1
                if self.tree[pos] >= value:
                    return
                self.tree[pos] = value
                while pos > 1:
                    pos >>= 1
                    new_val = max(self.tree[2*pos], self.tree[2*pos+1])
                    if self.tree[pos] == new_val:
                        break
                    self.tree[pos] = new_val
            
            def query_range(self, l, r):
                # 查询 [l, r] 的最大值，1-based
                res = 0
                l += self.n - 1
                r += self.n - 1
                while l <= r:
                    if l % 2 == 1:
                        res = max(res, self.tree[l])
                        l += 1
                    if r % 2 == 0:
                        res = max(res, self.tree[r])
                        r -= 1
                    l >>= 1
                    r >>= 1
                return res

        n = len(nums)
        if n == 0:
            return 0
        max_val = 10**5  # 题目中 nums[i] <= 1e5
        st_down = SegmentTree(max_val)  # 维护 down[a]（必须选a，下降结尾）
        st_up = SegmentTree(max_val)    # 维护 up[a]（必须选a，上升结尾）
        
        up = [0] * n
        down = [0] * n
        res = 0
        
        for i in range(n):
            x = nums[i]
            # 先将 a = i - k 加入线段树（进入可用范围）
            a = i - k
            if a >= 0:
                st_down.update(nums[a], down[a])
                st_up.update(nums[a], up[a])
            
            # 计算 up[i]：找 nums[a] < x 的最大 down[a]
            max_d = 0
            if x - 1 >= 1:
                max_d = st_down.query_range(1, x-1)
            up[i] = max_d + x
            
            # 计算 down[i]：找 nums[a] > x 的最大 up[a]
            max_u = 0
            if x + 1 <= max_val:
                max_u = st_up.query_range(x+1, max_val)
            down[i] = max_u + x
            
            # 更新全局最大值
            res = max(res, up[i], down[i])
        
        return res