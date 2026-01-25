# 1 based index ,往0 插入则会出错
# 如果有 array initial 操作，用1 based 更自然，因为 self.tree = [0] + list(size_or_arr) + [0] 这里有了1 的偏移
class FenwickTree:
    def __init__(self, size_or_arr):
        if isinstance(size_or_arr, int):
            self.size = size_or_arr
            self.tree = [0] * (self.size + 2)
        else:
            # 1. 记录大小
            self.size = len(size_or_arr)
            # 2. 初始化 tree，注意第一个元素（下标0）不用，从下标1开始存入原数组
            self.tree = [0] + list(size_or_arr) + [0]
            # 3. 调用线性构建
            self._build()

    def _build(self):
        """
        线性构建方法：每个节点将其前缀和贡献传递给其直接父节点。
        """
        for i in range(1, self.size + 1):
            j = i + (i & -i)  # 寻找父节点下标
            if j <= self.size:
                self.tree[j] += self.tree[i]

    def add(self, index, delta=1):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

    def bisect_min_larger(self, target):
        index = 0
        bit_mask = 1 << (self.size.bit_length() - 1)

        while bit_mask > 0:
            next_index = index + bit_mask
            if next_index <= self.size and self.tree[next_index] < target:
                target -= self.tree[next_index]
                index = next_index
            bit_mask >>= 1
        
        # After the loop, `index` is the largest prefix sum less than `target`.
        # The next index is the smallest prefix sum greater than or equal to `target`.
        return index + 1
    
    def rsum(self, left: int, right: int) :
        assert 0 <= left <= right <= self.size
        if left > right:
            return 0
        if left == 0:
            return self.sum(right)
        
        return self.sum(right) - self.sum(left - 1)