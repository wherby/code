# Binaray ops

Or and And 有单调性，所以可以用trick，从当前数字到以前的子数组只能有32个值
Xor 没有单调性，只能用hash计数 

# SubArray Log-trick
[SubArray LogTrick](../../array/subarray-logTrick)


# 线性基 XorBasis

在数组用选择数字使得xor值最大 

[XorBasis](线性基/XorBasis.py)

把数组分为两个子数组的xor值的和最大：在置位和为奇数的位置上的划分没有意义，所以在加入线性基的时候异或 ~xor 值，因为xor 记录了所有奇数个置位的值，~xor就是偶数个置位的mask 所以数字与mask and之后就只留下了偶数位置位的数值

[把数组分为两个子数组的xor值的和最大](线性基/把数组分成两个数列Xor和最大值.py)