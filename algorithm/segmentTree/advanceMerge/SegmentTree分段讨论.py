# https://codeforces.com/problemset/problem/2057/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0612/solution/cf2057d.md
# 线段树在处理 max(𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟)−min(𝑎𝑙,𝑎𝑙+1,…,𝑎𝑟)−(𝑟−𝑙) 的最值的时候
# 首先，对于区间[l,r]考虑最小的包含区间最大值最小值的子区间，则取这个子区间不影响极差，但使得长度变小了，所以是更优的。因此最终答案中，一定一个边缘是最大值，一个边缘是最小值。
# 把它分解为左右端点最大，最小值的两种情况，把求值表达式分解为每个线段的最值表达式，再用两种情况分别计算
import sys
sys.path.append("..")
from cflibs.cflibs import *

inf = 2 * 10 ** 9

class SegTree:
    def __init__(self,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        
        self._mi1 = [inf] * (2 * self._size)
        self._ma1 = [-inf] * (2 * self._size)
        self._mi2 = [inf] * (2 * self._size)
        self._ma2 = [-inf] * (2 * self._size)
        self._ans = [0] * (2 * self._size)
        
        for i in range(self._n):
            self._mi1[self._size + i] = v[i] - i
            self._ma1[self._size + i] = v[i] - i
            self._mi2[self._size + i] = v[i] + i
            self._ma2[self._size + i] = v[i] + i
        
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p0 = p
        p += self._size
        self._mi1[p] = x - p0
        self._ma1[p] = x - p0
        self._mi2[p] = x + p0
        self._ma2[p] = x + p0
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def all_prod(self) -> typing.Any:
        return self._ans[1]

    def _update(self, k: int) -> None:
        self._mi1[k] = fmin(self._mi1[2 * k], self._mi1[2 * k + 1])
        self._ma1[k] = fmax(self._ma1[2 * k], self._ma1[2 * k + 1])
        self._mi2[k] = fmin(self._mi2[2 * k], self._mi2[2 * k + 1])
        self._ma2[k] = fmax(self._ma2[2 * k], self._ma2[2 * k + 1])
        self._ans[k] = fmax(self._ans[2 * k], self._ans[2 * k + 1])
        self._ans[k] = fmax(self._ans[k], self._ma1[2 * k + 1] - self._mi1[2 * k])
        self._ans[k] = fmax(self._ans[k], self._ma2[2 * k] - self._mi2[2 * k + 1])

def main():
    t = II()
    outs = []

    for _ in range(t):
        n, q = MII()
        nums = LII()
        
        seg = SegTree(nums)
        outs.append(seg.all_prod())
        
        for _ in range(q):
            idx, val = MII()
            idx -= 1
            
            seg.set(idx, val)
            outs.append(seg.all_prod())

    print('\n'.join(map(str, outs)))