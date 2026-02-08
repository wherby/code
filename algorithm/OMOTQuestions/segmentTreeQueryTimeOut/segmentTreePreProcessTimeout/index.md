# https://leetcode.cn/problems/minimum-stability-factor-of-array/submissions/641582147/
# SegmentTree pre process will timeout



# https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/submissions/
使用错误的方式求LIS的时候会OT， 维护单调队列比使用BIT或者Segment Tree的速度快，因为后者是固定的LogN 复杂度，前者 是Logn,其中n 是从0 增长到m  m<N 