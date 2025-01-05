
https://leetcode.cn/problems/my-calendar-ii/submissions/338722637/?envType=daily-question&envId=2025-01-03

在 algorithm/sortedContainers/sorteddict/my-calendar-ii/q731.2.py 用了SortedDict 在遍历值的时候由于是有序的，就免去了再排序的操作

在这个题目的解法中采用了先操作 再反悔的 应用

``` python
    def book(self, startTime: int, endTime: int) -> bool:
        self.sd[startTime] = self.sd.get(startTime, 0) + 1
        self.sd[endTime] = self.sd.get(endTime, 0) - 1
        s = 0
        for v in self.sd.values():
            s += v
            if s > 2:
                self.sd[startTime] -= 1
                self.sd[endTime] += 1
                return False
        return True
```

如果不采用这种操作，则需要复制全状态

```python
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newHeap = list(self.st)
        heapq.heappush(newHeap, (start,1))
        heapq.heappush(newHeap, (end-0.1,-1))
        acc =0
        while newHeap:
            _, diff = heapq.heappop(newHeap)
            acc += diff
            if acc >=3:
                return False
        heapq.heappush(self.st, (start,1))
        heapq.heappush(self.st, (end-0.1,-1))
        return True
```