# 子数组and


## OR
子数组or 利用了每个数字加入之后，以这个数字结尾的子数组的or的状态一定只有32个（数字位数决定）这一性质可以进行递推dp
algorithm\array\subarray\AndOrToK\find-subarray-with-bitwise-or-closest-to-k copy.py

## And
algorithm\array\subarray\AndOrToK\number-of-subarrays-with-and-value-of-k.py
子数组and 利用了每个数字加入之后，以这个数字结尾的子数组的and的状态一定只有32个（数字位数决定）这一性质可以进行递推dp

如果用线段树解决则会OT: 
https://leetcode.cn/contest/biweekly-contest-134/problems/number-of-subarrays-with-and-value-of-k/submissions/
contest\00000c397d130\d134\q4

