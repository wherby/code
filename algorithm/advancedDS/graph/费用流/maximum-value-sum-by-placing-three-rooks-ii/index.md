
# 
https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/solutions/2884186/qian-hou-zhui-fen-jie-pythonjavacgo-by-e-gc48/
附：费用流做法
建图：

把第 i 行看作节点 i，第 j 列看作节点 m+j。
创建一个完全二分图，在第 i 行到第 j 列之间连边，容量为 1，费用为 −grid[i][j]。因为我们求的是最小费用流，取负号转成求最大费用流。
从超级节点 R=m+n 向所有行节点 0,1,2,⋯,m−1 连边，容量为 1，费用为 0。
从所有列节点 m,m+1,m+2,⋯,m+n−1 向超级节点 C=m+n+1 连边，容量为 1，费用为 0。
从超级源点 S=m+n+2 向 R 连边，容量为 3，费用为 0。如果题目要放置 4 个车，甚至 k 个车，只需把这里的 3 改成 k 即可。
这样建图可以保证三个车不会同行同列（否则节点 i 或者节点 m+j 的流量会超过 1，也就是超过容量）。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-value-sum-by-placing-three-rooks-ii/solutions/2884186/qian-hou-zhui-fen-jie-pythonjavacgo-by-e-gc48/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。