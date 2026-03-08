# 用递归的方式得到生成序列的值
# 分析k在序列的位置，分情况讨论：
# 1. k在前半部分，直接递归调用findKthBit(n-1, k)
# 2. k在中间位置，直接返回1
# 3. k在后半部分，递归调用findKthBit(n-1, (1 << n) - k)，并将结果取反返回

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        if k == 1 << (n - 1):
            return '1'
        if k < 1 << (n - 1):
            return self.findKthBit(n - 1, k)
        res = self.findKthBit(n - 1, (1 << n) - k)
        return '0' if res == '1' else '1'

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-kth-bit-in-nth-binary-string/solutions/3908610/liang-chong-xie-fa-di-gui-die-dai-python-je8p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。