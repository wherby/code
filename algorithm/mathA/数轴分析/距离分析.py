# https://leetcode.cn/problems/number-of-perfect-pairs/description/
#给你一个整数数组 nums。

# 如果一对下标 (i, j) 满足以下条件，则称其为 完美 的：
# i < j
# 令 a = nums[i]，b = nums[j]。那么：
# min(|a - b|, |a + b|) <= min(|a|, |b|)
# max(|a - b|, |a + b|) >= max(|a|, |b|)
# 返回 不同 完美对 的数量。

# 分析距离，第二个不等式恒成立，第一个不等式成立的条件是 min(abs(a),abs(b)) *2 >= max(abs(a),abs(b)) 所以可以用双指针解决