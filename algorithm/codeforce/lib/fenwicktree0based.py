class FenwickTree:
    def __init__(self, size):
        self.size = size
        # 0-based 索引，所以数组大小为 size
        self.tree = [0] * self.size

    def add(self, index, delta=1):
        # 0-based to 1-based index conversion
        index += 1
        while index <= self.size:
            self.tree[index - 1] += delta
            index += index & -index

    def sum(self, index):
        res = 0
        # 0-based to 1-based index conversion
        index += 1
        while index > 0:
            res += self.tree[index - 1]
            index -= index & -index
        return res

    def bisect_min_larger(self, target):
        index = -1
        bit_mask = 1 << (self.size.bit_length() - 1)
        
        while bit_mask != 0:
            next_index = index + bit_mask
            # 确保 next_index 在 0-based 索引范围内
            if next_index < self.size and self.tree[next_index] < target:
                target -= self.tree[next_index]
                index = next_index
            bit_mask >>= 1
        
        # 结果为 0-based 索引
        return index + 1