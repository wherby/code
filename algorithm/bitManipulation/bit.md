# int to binary 把int 转换为指定的2进制
>>> a =2
>>> '{:08b}'.format(a)
'00000010'
>>> '{:032b}'.format(a) 
'00000000000000000000000000000010'

## [All bit state for DP](https://wherby.github.io/code/algebra/all-submasks.html)


## bit control for 10**5 length
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1
        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-total-reward-using-operations-ii/solutions/2805413/bitset-you-hua-0-1-bei-bao-by-endlessche-m1xn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

a.bit_length() 得到最高位


##  bit count 
https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/?envType=daily-question&envId=2024-11-02
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return -1 if n &k != k else (n^k).bit_count()

# 最低位
选取最低位,去除最低位
>>> a = 14
>>> a&(-a)
2
>>> a&(a-1)
12

