


# 

模版查找 “root.left.isTracked = root.right.isTracked = root.isTracked” 发现有很多题目用这个模版解决，但是这个模版其实不是很通用

algorithm/segmentTree/动态开点/wrongVersion/DynamicSegTree.querybool.py 虽然可以pass，但是 function 在不是bool的情况下会有问题

```
    def _pushDown(self, root: Node) -> None:
        if not root.left:
            root.left = Node()
        if not root.right:
            root.right = Node()
        if root.lazy:
            root.left.lazy = root.right.lazy = True
            root.left.isTracked = root.right.isTracked = root.isTracked
            root.lazy = False
```


query 的时候也不是从value 得到的值，改变成其它用途的时候，也会很难

```py
    def _query(self, L: int, R: int, l: int, r: int, root: Node) -> bool:
        if L <= l <= r <= R:
            return root.isTracked

        self._pushDown(root)
        mid = (l + r) >> 1
        res = True
        if L <= mid:
            res = res and self._query(L, R, l, mid, root.left)
        if R >= mid + 1:
            res = res and self._query(L, R, mid + 1, r, root.right)
        return res
```