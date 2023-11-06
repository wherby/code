from testInput import *
from typing import List, Tuple, Optional

def lowbit(x):
    return x & (-x)

class BIT:
    def __init__(self, n):
        self.n = n
        self.a = [0] * (n + 1)
        self.sum = [0] * (n + 1)
    
    def update(self, pos, val):
        if not pos:
            return
        idx = pos
        while True:
            idx += lowbit(idx)
            if idx > self.n:
                break
            start = idx - lowbit(idx)
            self.sum[idx] += val * (pos - start)
        idx = pos
        while idx > 0:
            self.a[idx] += val
            idx -= lowbit(idx)
    
    def query(self, pos):
        if not pos:
            return 0
        res = 0
        idx = pos
        while True:
            idx += lowbit(idx)
            if idx > self.n:
                break
            start = idx - lowbit(idx)
            res += self.a[idx] * (pos - start)
        idx = pos
        while idx > 0:
            res += self.sum[idx]
            deg = lowbit(idx)
            res += self.a[idx] * deg
            idx -= deg
        return res

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mp = {}
        n = len(nums)
        tree = BIT(n)
        res = tot = tot2 = 0
        for i,val in enumerate(nums):
            prev = mp.get(val, -1)
            ssum = tot2 - ((i + i - prev) * (prev + 1) // 2 - tree.query(prev + 1))
            if prev ==0:
                print(tree.query(i+1),tree.query(prev+1),i,prev)
                print(ssum,tree.query(i+1) - tree.query(prev+1),i-prev,i,prev)
            tot += ssum + ssum + (i - prev)
            res += tot
            tot2 += i - prev
            tree.update(prev + 1, 1)
            mp[val] = i
        print(tree.sum[:317])
        print(tree.a[:317])
        print(tree.query(317),tree.query(1))
        return res % (10 ** 9 + 7)
    
import time

start = time.time()
re =Solution().sumCounts(nums)
print(re)
end = time.time()
print(end - start)