# 1 based index ,往0 插入则会出错
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)  # 1-based indexing

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