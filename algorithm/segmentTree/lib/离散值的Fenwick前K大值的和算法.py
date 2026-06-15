# https://leetcode.cn/problems/maximum-subarray-sum-after-at-most-k-swaps/description/
import math

class Fenwick:
    def __init__(self, size: int):
        self.tree = [[0, 0] for _ in range(size)]
        self.size = size

    def update(self, i: int, num: int, val: int):
        while i < self.size:
            self.tree[i][0] += num
            self.tree[i][1] += val
            i += i & -i

    def kth(self, k: int, sorted_arr: list[int]) -> int:
        i = 0
        b = 1 << 10  
        while b > 0:
            nxt = i | b
            if nxt < self.size and self.tree[nxt][0] < k:
                k -= self.tree[nxt][0]
                i = nxt
            b >>= 1
        
        # --- 顺从直觉的黄金修正 ---
        target_rank = i + 1 # 目标就在第 i + 1 个柜子
        
        # 换算成 Python 的 0-based 下标：(i + 1) - 1 = i
        # 别忘了处理越界保护：如果整个树是空的，target_rank 可能会超出 sorted_arr 的范围
        if i < len(sorted_arr):
            return sorted_arr[i]
        return sorted_arr[-1]

    def pre_sum(self, k: int, sorted_arr: list[int]) -> int:
        i = 0
        res = 0
        b = 1 << 10
        while b > 0:
            nxt = i | b
            if nxt < self.size and self.tree[nxt][0] < k:
                k -= self.tree[nxt][0]
                res += self.tree[nxt][1]
                i = nxt
            b >>= 1
            
        # --- 顺从直觉的黄金修正 ---
        # 1 到 i 号柜子已经全额打包进 res 了
        # 剩下的 k 个零头名额，同样必须去第 i + 1 个柜子里强行扣除！
        if i < len(sorted_arr):
            res += sorted_arr[i] * k  # 这里的 sorted_arr[i] 就是第 i + 1 个柜子的物理值
            
        return res

    def clone(self):
        new_f = Fenwick(self.size)
        new_f.tree = [item[:] for item in self.tree]
        return new_f


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        sorted_arr = sorted(list(set(nums)))
        m = len(sorted_arr)
        n = len(nums)
        if len([a for a in nums if a >0]) ==0:
            return max(nums)
        if len([a for a in nums if a<0]) <=k:
            return sum([a for a in nums if a >0]) 

        # 建立标准的 1-based 树状数组排名
        val_to_rank = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
        rank = [val_to_rank[x] for x in nums]

        out_tree_all = Fenwick(m + 1)
        total_sum = 0
        for i, x in enumerate(nums):
            out_tree_all.update(rank[i], 1, x)
            total_sum += x

        ans = -math.inf

        for left in range(n):
            in_tree = Fenwick(m + 1)
            out_tree = out_tree_all.clone()
            need_swap = 0
            sub_sum = 0

            for right in range(left, n):
                x = nums[right]
                rk = rank[right]
                sub_sum += x
                
                in_tree.update(rk, 1, x)
                out_tree.update(rk, -1, -x)

                ok = False
                sz = right - left + 1
                
                if need_swap < k and need_swap < sz and need_swap < n - sz:
                    if in_tree.kth(need_swap + 1, sorted_arr) < out_tree.kth(n - sz - need_swap, sorted_arr):
                        ok = True
                        need_swap += 1

                if not ok and need_swap > 0:
                    if in_tree.kth(need_swap, sorted_arr) >= out_tree.kth(n - sz - need_swap + 1, sorted_arr):
                        need_swap -= 1

                delta = 0
                if need_swap > 0:
                    in_sum = in_tree.pre_sum(need_swap, sorted_arr)
                    out_sum = total_sum - sub_sum - out_tree.pre_sum(n - sz - need_swap, sorted_arr)
                    delta = out_sum - in_sum

                ans = max(ans, sub_sum + delta)

        return ans