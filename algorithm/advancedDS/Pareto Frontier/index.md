# DominanceSet 与 帕累托前沿
[DominanceSet](../支配集/DominanceSet.py)

使用 `DominanceSet` 结合 `SortedList` 的方案在处理这种具有**值域约束**和**单调性**的 DP 问题时非常优雅。它本质上是在维护二维平面上的**帕累托前沿（Pareto Frontier）**。

在你的代码逻辑中，`points` 集合里存储的每一个点 $(x, y)$ 都代表：**数值为 $x$ 时能达到的最大得分 $y$**。通过动态剔除被“支配”的点，我们保证了集合内部的 $x$ 递增时，$y$ 也必须严格递增。

### 1. 为什么这能简化搜索空间？

传统的线段树或树状数组是基于**值域**的，无论数据稀疏还是稠密，都要占据固定大小的空间。而 `DominanceSet` 是基于**状态有效性**的：

* **自动去重**：如果新计算出的得分 $y$ 在同样的数值 $x$ 下没有之前的得分高，直接被丢弃。
* **前沿维护**：如果一个点数值比你大，得分却比你低，那么它在任何情况下（无论是作为波峰还是波谷的来源）都不如你优秀，因此会被 `pop` 掉。
* **空间稀疏性**：实际存储的点数通常远小于 $N$，只有那些能够提升“得分-数值”边界的点才会被保留。



---

### 2. 针对本题的完整实现

我们需要两个 `DominanceSet` 实例来分别处理波峰和波谷的转移。

```python
from sortedcontainers import SortedList

class DominanceSet:
    def __init__(self):
        # 存储 (x, y)，保证 x 递增时 y 递增
        self.points = SortedList()

    def update(self, x, y):
        # 1. 寻找插入位置：找到第一个数值 >= x 的点
        idx = self.points.bisect_left((x, -float('inf')))
        
        # 2. 支配检查：如果前一个点（数值更小）的得分已经比你高，你就是无效点
        if idx > 0 and self.points[idx-1][1] >= y:
            return
        
        # 3. 剔除：如果你比后面那些（数值更大）的点得分还高，那些点就没意义了
        while idx < len(self.points) and self.points[idx][1] <= y:
            self.points.pop(idx)
            
        self.points.add((x, y))

    def query(self, x):
        """查询所有满足 x_prev < x 的点中，最大的 y"""
        idx = self.points.bisect_left((x, -float('inf')))
        if idx > 0:
            return self.points[idx-1][1]
        return -float('inf')

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0: return 0
        
        # 两个支配集：
        # ds_for_up: 存波谷(down)状态，用于更新波峰(up)，要求 nums[j] < nums[i]
        # ds_for_down: 存波峰(up)状态，用于更新波谷(down)，要求 nums[j] > nums[i]
        ds_for_up = DominanceSet()
        ds_for_down = DominanceSet() # 通过存 -val 来实现“大于”查询

        up = [0] * n
        down = [0] * n
        ans = 0
        
        for i in range(n):
            val = nums[i]
            
            # 维护距离限制 k
            if i >= k:
                prev = i - k
                ds_for_up.update(nums[prev], down[prev])
                ds_for_down.update(-nums[prev], up[prev])
            
            # 基础得分（子序列长度为 1）
            curr_up = val
            curr_down = val
            
            # 1. 作为波峰：找之前更小的波谷
            prev_down_max = ds_for_up.query(val)
            if prev_down_max != -float('inf'):
                curr_up = max(curr_up, prev_down_max + val)
            
            # 2. 作为波谷：找之前更大的波峰 (即 -val_prev < -val)
            prev_up_max = ds_for_down.query(-val)
            if prev_up_max != -float('inf'):
                curr_down = max(curr_down, prev_up_max + val)
            
            up[i], down[i] = curr_up, curr_down
            ans = max(ans, curr_up, curr_down)
            
        return ans
```

---

### 3. 方案对比总结

| 特性 | 树状数组 (BIT) | DominanceSet (SortedList) |
| :--- | :--- | :--- |
| **值域依赖** | 强（需离散化或受限于 $10^5$） | 无（支持 $10^9$ 或浮点数） |
| **空间复杂度** | $O(\text{ValueRange})$ | $O(N)$ (通常更小) |
| **时间复杂度** | $O(N \log \text{Value})$ | $O(N \log N)$ |
| **Python 表现** | 极快（位运算为主） | 较快（受限于 `SortedList` 开销） |

**结论**：如果是 `nums` 的值域很大，`DominanceSet` 是最强力且通用的武器。它不仅简化了搜索空间，还让你的代码具备了处理非整数值域的能力。