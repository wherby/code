#  https://leetcode.cn/problems/convert-to-base-2/description/?envType=daily-question&envId=2024-04-28

class Solution:
    def baseNeg2(self, n: int) -> str:
        k = 1
        ans = []
        while n:
            if n % 2:
                ans.append('1')
                n -= k
            else:
                ans.append('0')
            n //= 2
            k *= -1
        return ''.join(ans[::-1]) or '0'

#作者：ylb
#链接：https://leetcode.cn/problems/convert-to-base-2/solutions/2210964/python3javacgotypescript-yi-ti-yi-jie-mo-5edi/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。