
# 线性基模板
class XorBasis:
    def __init__(self, n: int):
        self.n =n
        self.b = [0] * n

    def insert(self, x: int) -> None:
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if x >> i & 1:
                if b[i] == 0:
                    b[i] = x
                    return
                x ^= b[i]

    def max_xor(self) -> int:
        b = self.b
        res = 0
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res

    def check(self,x ):
        for i in range(self.n-1,-1,-1):
            if x&(1<<i):
                x ^=self.b[i]
        return x ==0

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/partition-array-for-maximum-xor-and-and/solutions/3734850/shi-zi-bian-xing-xian-xing-ji-pythonjava-3e80/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 为什么check 要从大到小遍历
# 线性基的 basis 数组是经过特殊构造的：basis[i] 的最高有效位（Most Significant Bit, MSB）恰好是第 i 位。这意味着，basis[i] 只能影响比它低的位，而不能影响比它高的位。
# 从高位到低位遍历 i，可以确保每一步的异或操作都只关注当前位：
# 当 x 的第 i 位为 1 时，我们用 basis[i] 去异或 x。由于 basis[i] 的 MSB 也是第 i 位，这个操作会把 x 的第 i 位变为 0。
# 更重要的是，basis[i] 的所有更高位都是 0，所以它不会影响 x 的更高位。
# 这个过程就像一个逐位消元的过程。我们从最高位开始，逐一将 x 的每一位“消掉”，直到 x 变为 0。如果最终 x 变为 0，说明原始的 x 可以由基中的元素异或得到。

if __name__ == '__main__':
    ls = [1,3,5,7,6,10,23,456]
    xorB = XorBasis(20)
    for a in ls:
        xorB.insert(a)
    print(xorB.max_xor())