

## 维护LazySegmentTree 的时候大于1 的区间长度
https://leetcode.cn/problems/separate-squares-ii/description/?envType=daily-question&envId=2026-01-14
转换为最小覆盖的区间长度的总长度
[特征函数生成](usage/lazySegmentTree函数编写.py)
```python
def getLeastCover(vd):
        # (left,right,lowestCover,lowerstCoverLength)
    E = (10**20,0,10**10,0)
    def op(x,y):
        x1,x2,x3,x4 = x 
        y1,y2,y3,y4 = y 
        mc = min(x3,y3)
        mcl = (x4 if x3 ==mc else 0) + (y4 if y3 == mc else 0)
        return   (min(x1,y1),max(x2,y2),mc,mcl)
    def mapping(v,x):
        x1,x2,x3,x4 = x 
        return (x1,x2,x3+v,x4)
    def composition(x,y):
        return x+y
    segTree = LazySegmentTree(m,op,E,mapping,composition,0)
    v = []
    for a,b in pairwise(vd):
        v.append((a,b,0,b-a))
    #print(v)
    segTree.build(v)
    return segTree
```
这里E 作为单位元向量需要能被合并切幂等，则 left 应该是大值，right应该是最小值，维护的cover次数应该是最大值，cover的长度应该为0
op 的时候，是区间合并，这时是合并区间长度都为最低覆盖次数的长度总和，同时把左右端点值合并
v 数组则是根据区间离散分别，生成区间的初始数组
