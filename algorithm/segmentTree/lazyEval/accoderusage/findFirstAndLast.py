# findlast is not verified.
class Node:
    __slots__ = 'min', 'max', 'todo'

    def __init__(self):
        self.min = self.max = self.todo = 0

class LazySegmentTree:
    def __init__(self, n: int):
        self._n = n
        # Calculate tree size: 2 * (next power of 2)
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]

    # Apply lazy tag to the current node's subtree
    def _apply(self, node: int, todo: int) -> None:
        cur = self._tree[node]
        cur.min += todo
        cur.max += todo
        cur.todo += todo

    # Push down lazy tag from the current node to its children
    def _spread(self, node: int) -> None:
        todo = self._tree[node].todo
        if todo == 0:  # No pending updates
            return
        self._apply(node * 2, todo)
        self._apply(node * 2 + 1, todo)
        self._tree[node].todo = 0  # Clear tag

    # Merge min/max values from children to the current node
    def _maintain(self, node: int) -> None:
        l_node = self._tree[node * 2]
        r_node = self._tree[node * 2 + 1]
        self._tree[node].min = min(l_node.min, r_node.min)
        self._tree[node].max = max(l_node.max, r_node.max)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # Current subtree is fully contained in [ql, qr]
            self._apply(node, f)
            return
        self._spread(node)
        m = (l + r) // 2
        if ql <= m:  # Update left child
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # Update right child
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _find_first(self, node: int, l: int, r: int, ql: int, qr: int, target: int) -> int:
        # Pruning condition: out of query range or target is outside current [min, max] range
        if l > qr or r < ql or not (self._tree[node].min <= target <= self._tree[node].max):
            return -1
        if l == r:
            return l
        self._spread(node)
        m = (l + r) // 2
        
        # Priority: Left child first (find the first/leftmost)
        idx = self._find_first(node * 2, l, m, ql, qr, target)
        if idx < 0:
            # Search right child if not found in left
            idx = self._find_first(node * 2 + 1, m + 1, r, ql, qr, target)
        return idx
    
    def _find_last(self, node: int, l: int, r: int, ql: int, qr: int, target: int) -> int:
        # Pruning condition: out of query range or target is outside current [min, max] range
        if l > qr or r < ql or not (self._tree[node].min <= target <= self._tree[node].max):
            return -1
        if l == r:
            # Since l==r is a leaf, and target is in [min, max], it must be the target value
            return l
        
        self._spread(node) # Push down lazy tag
        m = (l + r) // 2
        
        # 核心区别: Priority: Right child first (find the last/rightmost)
        idx = -1
        # 1. Search right child first
        if qr > m: # Ensure right child range is relevant
            idx = self._find_last(node * 2 + 1, m + 1, r, ql, qr, target)
        
        # 2. If not found in right child, search left child
        if idx < 0 and ql <= m: # If right failed and left child range is relevant
            idx = self._find_last(node * 2, l, m, ql, qr, target)
            
        return idx

    # 用 f 更新 [ql, qr] 中的每个 sum[i]
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 查询 [ql, qr] 内第一个等于 target 的元素下标
    # 找不到返回 -1
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def find_first(self, ql: int, qr: int, target: int) -> int:
        return self._find_first(1, 0, self._n - 1, ql, qr, target)

    # 查询 [ql, qr] 内最后一个等于 target 的元素下标
    # 找不到返回 -1
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def find_last(self, ql: int, qr: int, target: int) -> int:
        return self._find_last(1, 0, self._n - 1, ql, qr, target)