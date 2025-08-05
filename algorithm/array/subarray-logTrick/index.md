# 子数组 subarray

## 特性

子数组都可以用DP来递推，用加入数字作为结尾构成新的状态转移矩阵，如果and or的特性，则可以把转移状态压缩到位数n(32)


# Xor 模版

[Xor 其他应用](../../mathA/xor模板/xor.md)


# [smallest-subarrays-with-maximum-bitwise-or ](LogTrick和其他写法)

利用dp的思想，每个num[i]记录后面的数字对i开始的子数组影响，影响的次数一定会小于32次，用while控制向前传递的条件，只有影响了后一位才能影响前一位
