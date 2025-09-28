from typing import List, Tuple, Optional
MOD = 1_000_000_007

# a @ b，其中 @ 是矩阵乘法
# 更快的写法见另一份代码【NumPy】
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f1
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        k = r - l + 1
        m = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k - 1 - i):
                m[i][j] = 1

        f1 = [[1] for _ in range(k)]
        fn = pow_mul(m, n - 1, f1)
        return sum(row[0] for row in fn) * 2 % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-zigzag-arrays-ii/solutions/3794101/ju-zhen-kuai-su-mi-you-hua-dppythonnumpy-77e7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。