
https://leetcode.cn/problems/range-module/solution/python-dong-tai-kai-dian-xian-duan-shu-b-jrrs/


## 动态开点模版还是有问题 Timeout 




## latest version:
Modify based on https://leetcode.cn/problems/maximum-coins-from-k-consecutive-bags/description/

algorithm/segmentTree/动态开点/[LatestV]DynamicSegTreeWithFunction2 copy 3.py

algorithm/segmentTree/动态开点/v1.DynamicSegTreeWithFunction2.py


查找 “mid = (l + r) >> 1
        ## ## need to be changed, how to merge left,right value ”
这个值，发现以前很多模版可以AC但是也是模版有问题


```
    def _query(self, L: int, R: int, l: int, r: int, root: Node) :
        # self._pushDown(root,l,r) should be placed here
        if L <= l <= r <= R:
            return root.value
        self._pushDown(root,l,r)  # If pushdown move to after return ,there is bug 
        
        mid = (l + r) >> 1
        ## ## need to be changed, how to merge left,right value 
        ## set the initial res value for merge
        res = self.ret
        if L <= mid:
            res =self.merge(res, self._query(L, R, l, mid, root.left))
        if R >= mid + 1:
            res = self.merge(res,self._query(L, R, mid + 1, r, root.right))
        return res
```
可以看到很多已经“成功”的模版把 “self._pushDown(root,l,r)”放在return 后也是好的，其实不行，
在 algorithm/segmentTree/动态开点/wrongDS/wrongTest/maximum-coins-from-k-consecutive-bags.py 这里测试不可以通过