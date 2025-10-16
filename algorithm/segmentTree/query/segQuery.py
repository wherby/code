

class SegmentTree:
    """
    Implements a Max Segment Tree with a specialized query
    to find the rightmost index in a range [l, r] whose value > thr.
    The tree uses 1-based indexing internally for simplicity.
    """

    def __init__(self, arr: list[int]):
        """Initializes the Segment Tree."""
        # Original array (similar to C++ 'a')
        self.a = arr
        # Size of the original array (similar to C++ 'n')
        self.n = len(arr)
        
        # Tree array (t). We allocate 4*n space and use 1-based indexing.
        self.t = [0] * (4 * self.n)
        
        # Build the tree starting from root v=1, covering range [0, n-1]
        if self.n > 0:
            self._build(1, 0, self.n - 1)

    def _build(self, v: int, l: int, r: int):
        """Recursively builds the segment tree."""
        if l == r:
            # Leaf node stores the value from the original array
            self.t[v] = self.a[l]
            return
        
        m = (l + r) // 2
        
        # Left child: 2 * v (v << 1)
        self._build(2 * v, l, m)
        # Right child: 2 * v + 1 (v << 1 | 1)
        self._build(2 * v + 1, m + 1, r)
        
        # Internal node stores the maximum of its children
        self.t[v] = max(self.t[2 * v], self.t[2 * v + 1])

    def _query(self, v: int, l: int, r: int, ql: int, qr: int, thr: int) -> int:
        """
        Recursive helper for the specialized query.
        Finds the rightmost index k in [ql, qr] such that a[k] > thr.
        
        v: current node index
        l, r: range covered by node v
        ql, qr: query range
        thr: threshold
        """
        
        # Pruning 1: Current segment is outside the query range
        if qr < l or r < ql:
            return -1
        
        # Pruning 2: The maximum value in the current segment is not > threshold
        if self.t[v] <= thr:
            return -1

        # Base case: Found the required index (must be a leaf node)
        if l == r:
            # Since we passed the max(t[v]) > thr check, this is the answer
            return l

        m = (l + r) // 2
        
        # CRUCIAL: Search the right child first to ensure we find the rightmost index
        # (v << 1 | 1) -> 2 * v + 1
        res = self._query(2 * v + 1, m + 1, r, ql, qr, thr)
        
        if res != -1:
            # Found the answer in the right half, return immediately
            return res
        
        # If not found in the right half, search the left half
        # (v << 1) -> 2 * v
        return self._query(2 * v, l, m, ql, qr, thr)

    def query(self, l: int, r: int, thr: int) -> int:
        """
        Public facing query method. Finds the ***rightmost*** index in [l, r]
        with a value strictly greater than thr. Returns -1 if none found.
        """
        if l > r or self.n == 0:
            return -1
            
        # Start recursion from root (v=1), covering the full data range [0, n-1]
        return self._query(1, 0, self.n - 1, l, r, thr)


if __name__ == '__main__':
    # --- Example Usage ---

    # Example array: [2, 5, 1, 8, 3, 6]
    # Indices:       [0, 1, 2, 3, 4, 5]
    data = [2, 5, 1, 8, 3, 6]
    st = SegmentTree(data)

    # Query 1: Find rightmost index in [0, 5] with value > 5
    # Expected: Index 5 (value 6)
    result1 = st.query(0, 5, 5) 

    # Query 2: Find rightmost index in [0, 2] with value > 2
    # Expected: Index 1 (value 5)
    result2 = st.query(0, 2, 2) 

    # Query 3: Find rightmost index in [4, 5] with value > 6
    # Expected: -1 (Max value is 6, which is not > 6)
    result3 = st.query(4, 5, 6) 

    # Query 4: Find rightmost index in [0, 3] with value > 7
    # Expected: Index 3 (value 8)
    result4 = st.query(0, 3, 7) 

    print(f"Array: {data}")
    print(f"Query [0, 5], thr=5 -> Index: {result1}")
    print(f"Query [0, 2], thr=2 -> Index: {result2}")
    print(f"Query [4, 5], thr=6 -> Index: {result3}")
    print(f"Query [0, 3], thr=7 -> Index: {result4}")
