
## 原题

给你一个二维整数数组 intervals ，其中 intervals[i] = [starti, endi] 表示从 starti 到 endi 的所有整数，包括 starti 和 endi 。

包含集合 是一个名为 nums 的数组，并满足 intervals 中的每个区间都 至少 有 两个 整数在 nums 中。

例如，如果 intervals = [[1,3], [3,7], [8,9]] ，那么 [1,2,4,7,8,9] 和 [2,3,4,8,9] 都符合 包含集合 的定义。
返回包含集合可能的最小大小。

如果只有2，则很简单
```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ret = []
        for a,b in intervals:
            if len(ret) and a<= ret[-1]<=b and a<=ret[-2]<=b:
                continue 
            if len(ret) == 0 or a >ret[-1]:
                ret.append(b-1)
                ret.append(b)
                
            elif a<=ret[-1]<=b and a>ret[-2]:
                if ret[-1]== b:
                    ret.pop()
                    ret.append(b-1)
                    ret.append(b)
                else:
                    ret.append(b)
        #print(ret,intervals)
        return len(ret)
```

但是如果变成 K 个数字， 则复杂度就不能枚举了，可能需要用线段树标记，但是线段树标记又会有区间破裂的问题，必然 前面  【l,r】 已经标记了， 需要标记 K个连续的区域，需要跨越多个已经标记的
区域，这时就可以把对应区域弹出然后重新标记，弹出过程就是栈，而线段树是为了获取前缀和，则把前缀和集成在栈 里就可以完成


```python
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # 栈中保存闭区间左右端点，栈底到栈顶的区间长度的和
        st = [(-2, -2, 0)]  # 哨兵，保证不和任何区间相交
        for start, end in intervals:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d = 2 - (st[-1][2] - s)  # 去掉运行中的时间点
            if start <= r:  # start 在区间 st[i] 内
                d -= r - start + 1  # 去掉运行中的时间点
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # 剩余的 d 填充区间后缀
                l, r, _ = st.pop()
                d += r - l + 1  # 合并区间
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]
```