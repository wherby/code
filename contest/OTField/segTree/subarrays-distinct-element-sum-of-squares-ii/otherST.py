from testInput import *
from collections import defaultdict,deque
from typing import List, Tuple, Optional

class TreeNode(object):
    def __init__(self):
        self.left = -1
        self.right = -1
        self.sum_num = 0
        self.lazy_tag = 0


class Tree(object):
    def __init__(self, n, arr):
        self.n = n
        self.max_size = 4 * n
        self.tree = [TreeNode() for i in range(self.max_size)]  # 维护一个TreeNode数组
        self.arr = arr

    # index从1开始
    def _build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].sum_num = self.arr[left - 1]
        else:
            mid = (left + right) // 2
            self._build(index * 2, left, mid)
            self._build(index * 2 + 1, mid + 1, right)
            self.pushup_sum(index)

    # 构建线段树
    def build(self):
        self._build(1, 1, self.n)

    def _update2(self, ql, qr, val, i, l, r, ):
        mid = (l + r) // 2
        if l >= ql and r <= qr:
            self.tree[i].sum_num += (r - l + 1) * val  # 更新和
            self.tree[i].lazy_tag += val  # 更新懒惰标记
        else:
            self.pushdown_sum(i)
            if mid >= ql:
                self._update2(ql, qr, val, i * 2, l, mid)
            if qr > mid:
                self._update2(ql, qr, val, i * 2 + 1, mid + 1, r)
            self.pushup_sum(i)

    # 区间修改
    def update2(self, ql, qr, val, ):
        self._update2(ql, qr, val, 1, 1, self.n)

    def _query2(self, ql, qr, i, l, r, ):
        if l >= ql and r <= qr:  # 若当前范围包含于要查询的范围
            return self.tree[i].sum_num
        else:
            self.pushdown_sum(i)  # modify
            mid = (l + r) // 2
            res_l = 0
            res_r = 0
            if ql <= mid:  # 左子树最大的值大于了查询范围最小的值-->左子树和需要查询的区间交集非空
                res_l = self._query2(ql, qr, i * 2, l, mid, )
            if qr > mid:  # 右子树最小的值小于了查询范围最大的值-->右子树和需要查询的区间交集非空
                res_r = self._query2(ql, qr, i * 2 + 1, mid + 1, r, )
            return res_l + res_r

    def query2(self, ql, qr):
        return self._query2(ql, qr, 1, 1, self.n)

    # 求和,向上更新
    def pushup_sum(self, k):
        self.tree[k].sum_num = self.tree[k * 2].sum_num + self.tree[k * 2 + 1].sum_num

    # 向下更新lazy_tag
    def pushdown_sum(self, i):
        lazy_tag = self.tree[i].lazy_tag
        if lazy_tag != 0:  # 如果有lazy_tag
            self.tree[i * 2].lazy_tag += lazy_tag  # 左子树加上lazy_tag
            self.tree[i * 2].sum_num += (self.tree[i * 2].right - self.tree[i * 2].left + 1) * lazy_tag  # 左子树更新和
            self.tree[i * 2 + 1].lazy_tag += lazy_tag  # 右子树加上lazy_tag
            self.tree[i * 2 + 1].sum_num += (self.tree[i * 2 + 1].right - self.tree[
                i * 2 + 1].left + 1) * lazy_tag  # 右子树更新和
            self.tree[i].lazy_tag = 0  # 将lazy_tag 归0

    # 深度遍历
    def _show_arr(self, i):
        if self.tree[i].left == self.tree[i].right and self.tree[i].left != -1:
            print(self.tree[i].sum_num, end=" ")
        if 2 * i < len(self.tree):
            self._show_arr(i * 2)
            self._show_arr(i * 2 + 1)

    # 显示更新后的数组的样子
    def show_arr(self, ):
        self._show_arr(1)

    def __str__(self):
        return str(self.tree)

MOD=10**9+7
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        arr = [0]*(n+1)
        tree = Tree(n+1, arr)
        tree.build()
        
        pre=defaultdict(lambda:-1)
        res=[0]*n
        ans=0
        for i,x in enumerate(nums):
            if i==0:
                res[0]=1
            else:
                res[i]=res[i-1]+2*tree.query2(pre[x]+2,i+1)+i-pre[x]
            ans+=res[i]
            ans%=MOD
            tree.update2(pre[x]+2,i+1,1)
            # print(pre, tree.query2(1,i+1))
            pre[x]=i
        return ans

import time

start = time.time()
re =Solution().sumCounts(nums)
print(re)
end = time.time()
print(end - start)