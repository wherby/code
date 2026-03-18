# 如果 rsum 不是 sum(right) - sum(left-1)  
#.    是 sum(right) - sum(left) 则 fen_pre.rsum(idx, n) 在idx点上的积累  是0 因为idx点上的值会被减去 ，   fen_suf.rsum(0, idx) 在 idx点上积累也是0 因为 fen_suf.add(idx + 1, x * rev_pows[idx] % mod)

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

    def rsum(self, left: int, right: int) :
        #assert 0 <= left <= right <= self.size
        if left > right:
            return 0
        if left == 0:
            return self.sum(right)
        
        return self.sum(right) - self.sum(left - 1)

def reversePairs(arr):
    # 离散化
    sorted_arr = sorted(set(arr))
    rank = {v: i for i, v in enumerate(sorted_arr)}
    m =len(sorted_arr)
    fenw = FenwickTree(m)
    count = 0
    # 使用从后到前遍历的方式，确保在查询时 Fenwick Tree 中已经包含了当前元素之后的元素，使得Fenwick Tree查询的时候使用单元素查询，而不是区间查询，避免了idx点上的值被减去的情况
    for x in reversed(arr):
        r = rank[x]
        count += fenw.sum(r - 1)  # 查询 Fenwick Tree 中比当前元素小的数量
        fenw.add(r)  # 将当前元素加入 Fenwick Tree
    
    return count