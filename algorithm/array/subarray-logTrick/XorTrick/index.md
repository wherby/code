

## Xor 计算， 求递推式
https://leetcode.cn/contest/weekly-contest-413/problems/maximum-xor-score-subarray-queries/description/

https://zhwebsite.com/2024/09/01/leetcode-contest-413/
解答：这题脑筋急转弯。用几个例子试验一下，就能知道x到y的数组异或值XOR[x][y] = XOR[x][y-1] ^ XOR[x+1][y]。之后就退化成区间最大值了。

数组的异或值
下文用 ⊕ 表示异或。

考虑数组的异或值（最后剩下的元素）是由哪些元素异或得到的。

例如数组为 [a,b,c]，那么操作一次后变成 [a⊕b, b⊕c]，再操作一次，得到 a⊕b⊕b⊕c。其中 b 异或了 2 次。

为方便描述，下面把 a⊕b 简记为 ab，把 a⊕b⊕b⊕c 简记为 ab2c

又例如数组为 [a,b,c,d]，那么操作一次后变成 [ab,bc,cd]，再操作一次，变成 [ab2c,bc2d]，再操作一次，得到 ab3c3d。
可以发现，ab3c3d 相当于数组 [a,b,c] 的异或值，再异或 [b,c,d] 的异或值。

f[i][j] = f[i][j - 1] ^ f[i + 1][j]

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-xor-score-subarray-queries/solutions/2899932/qu-jian-dp-tao-qu-jian-dppythonjavacgo-b-w4be/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

[XorTrick](XorTrick.py)
Xor 操作可以用前缀和抵消，使用时序TireTree 查询