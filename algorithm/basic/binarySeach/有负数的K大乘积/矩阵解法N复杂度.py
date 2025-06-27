from typing import List, Tuple, Optional

from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        i0 = bisect_left(a, 0)  # 四个区域的水平分界线
        j0 = bisect_left(b, 0)  # 四个区域的垂直分界线

        def check(mx: int) -> bool:
            if mx < 0:
                cnt = 0

                # 右上区域
                i, j = 0, j0
                while i < i0 and j < m:  # 不判断 cnt < k 更快
                    if a[i] * b[j] > mx:
                        j += 1
                    else:
                        cnt += m - j
                        i += 1

                # 左下区域
                i, j = i0, 0
                while i < n and j < j0:
                    if a[i] * b[j] > mx:
                        i += 1
                    else:
                        cnt += n - i
                        j += 1
            else:
                # 右上区域和左下区域的所有数都 <= 0 <= mx
                cnt = i0 * (m - j0) + (n - i0) * j0

                # 左上区域
                i, j = 0, j0 - 1
                while i < i0 and j >= 0:
                    if a[i] * b[j] > mx:
                        i += 1
                    else:
                        cnt += i0 - i
                        j -= 1

                # 右下区域
                i, j = i0, m - 1
                while i < n and j >= j0:
                    if a[i] * b[j] > mx:
                        j -= 1
                    else:
                        cnt += j - j0 + 1
                        i += 1

            return cnt >= k

        n, m = len(a), len(b)
        corners = (a[0] * b[0], a[0] * b[-1], a[-1] * b[0], a[-1] * b[-1])
        left, right = min(corners), max(corners)
        return left + bisect_left(range(left, right), True, key=check)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/solutions/1050962/fen-lei-tao-lun-er-fen-da-an-by-endlessc-nl81/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。