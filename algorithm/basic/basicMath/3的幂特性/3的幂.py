
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/power-of-three/solutions/2974674/o1-shu-xue-zuo-fa-yi-xing-gao-ding-pytho-w0uh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 如果 n 是 3 的幂。由于任何 3 的幂都是 3 **19 的因子，所以 3 **19 modn=0。或者说 n 的某个倍数等于 3 **19 。
# 如果 n 不是 3 的幂。那么 n 必然有不等于 3 的质因子，所以 n 的倍数不可能等于 3 **19 这个只含质因子 3 的数
print(3**19)