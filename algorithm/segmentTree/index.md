# 线段树使用

## 线段树维护统计特性
利用Lazy线段树记录奇偶统计的影响力累加，然后使用线段树统计区域统计和的最大最小值，
题目需要找到最长的奇偶平衡串，利用影响力标记，在最后出现的时候到最后标记，记录当前标记总和，然后在线段树前面查询最左点的统计值不包含当前值，则证明从0到该点没有经过当前值，下一个点等于当前值，则可以找到平衡值的最长线段

[统计特性](lazyEval/accoderusage/mayTimeout-refine1.py)
[统计特性更快的版本](lazyEval/accoderusage/min_max_segTree.py)

## 线段树维护子数组特性
https://leetcode.cn/problems/maximum-subarray/solutions/228009/zui-da-zi-xu-he-by-leetcode-solution/ 方法二：分治
https://leetcode.cn/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solutions/3039428/liang-chong-fang-fa-xian-duan-shu-qian-h-961z/
前后缀求最大值
algorithm/segmentTree/segmentTreeNodeWithMerge.2.py
求不相连的最大值
algorithm/segmentTree/segmentTreeNodeWithMerge.py


# 
https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/

# 线段树OT 考虑SparseTable
algorithm/segmentTree/quickVersion/SparseTable.py
https://leetcode.cn/contest/biweekly-contest-160/problems/minimum-stability-factor-of-array/description/

[Use SpareTree to Speed up query for [l,r] query, only could be applied to [max, min, gcd] function can't be appied to [sum,xor,..]](../OMOTQuestions/segmentTreeQueryTimeOut/minimum-stability-factor-of-array/stTableAC.py)


# Quick version
quick version will AC for some scenario. for query/update will not run recursion. 

# min-max lazy segtree
[atcoder functional version may timeout ](lazyEval/accoderusage)
[min-max segment tree with find first from left ](lazyEval/accoderusage/noUseFunctional.py)
[min-max segment tree with find last from right](lazyEval/accoderusage/findFirstAndLast.py)

