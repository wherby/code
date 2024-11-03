

## 多状态表示

algorithm/segmentTree/节点多状态求值/OneIndex.py

        # 4 个数分别保存 f00, f01, f10, f11
        t = [[0] * 4 for _ in range(2 << n.bit_length())]

        # 手写 max，效率更高
        def max(a: int, b: int) -> int:
            return b if b > a else a

        # 合并左右儿子
        def maintain(o: int):
            a, b = t[o * 2], t[o * 2 + 1]
            t[o][0] = max(a[0] + b[2], a[1] + b[0])
            t[o][1] = max(a[0] + b[3], a[1] + b[1])
            t[o][2] = max(a[2] + b[2], a[3] + b[0])
            t[o][3] = max(a[2] + b[3], a[3] + b[1])


这里11表示前后都包含，状态表示的是合并的情况的限制，并不表示一定会取对应的值