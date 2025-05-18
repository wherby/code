# 
# https://leetcode.cn/problems/minimum-weighted-subgraph-with-the-required-paths-ii/description/
# 
#Problem D - 包含给定路径的最小带权子树 II
#解法：DFS & 倍增
#答案其实就是 src1，src2，dest 两两距离之和除以 2。

# 如果是N个点求最短路径，则需要按照DFS序排列之后求两两距离和除以2， 因为dfs序能保证路径上没有第三点

#用 DFS + 倍增在线求树上两点之间的距离即可。复杂度 O(nlogn)。不熟悉树上倍增的读者可以学习 leetcode 2846. 边权重均等查询。

