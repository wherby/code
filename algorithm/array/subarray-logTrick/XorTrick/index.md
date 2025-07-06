

## Xor 计算， 求递推式
https://leetcode.cn/contest/weekly-contest-413/problems/maximum-xor-score-subarray-queries/description/

https://zhwebsite.com/2024/09/01/leetcode-contest-413/
解答：这题脑筋急转弯。用几个例子试验一下，就能知道x到y的数组异或值XOR[x][y] = XOR[x][y-1] ^ XOR[x+1][y]。之后就退化成区间最大值了。