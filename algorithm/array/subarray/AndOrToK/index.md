# 子数组and


## OR
子数组or 利用了每个数字加入之后，以这个数字结尾的子数组的or的状态一定只有32个（数字位数决定）这一性质可以进行递推dp
algorithm\array\subarray\AndOrToK\find-subarray-with-bitwise-or-closest-to-k copy.py
algorithm/array/subarray/AndOrToK/shortest-subarray-with-or-at-least-k-ii.2.py


## And
algorithm\array\subarray\AndOrToK\number-of-subarrays-with-and-value-of-k.py
子数组and 利用了每个数字加入之后，以这个数字结尾的子数组的and的状态一定只有32个（数字位数决定）这一性质可以进行递推dp

如果用线段树解决则会OT: 
https://leetcode.cn/contest/biweekly-contest-134/problems/number-of-subarrays-with-and-value-of-k/submissions/
contest\00000c397d130\d134\q4


## And Or trick

求子数组的时候，以当前元素为结尾元素，然后 algorithm/array/subarray/AndOrToK/number-of-subarrays-with-and-value-of-k.2.py 这样循环
因为对前序序列和的改变只能有32次，所以看起来是N**2的复杂度，只有N*32 的复杂度

https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/solutions/2833497/jian-ji-xie-fa-o1-kong-jian-pythonjavacg-u7fv/

## LogTrick 
对于子数组特性具有单调性，则可以使用logtrick, 从当前点到以前的各个可能值域进行合并
algorithm/array/subarray/AndOrToK/logTrickForGCD.py


