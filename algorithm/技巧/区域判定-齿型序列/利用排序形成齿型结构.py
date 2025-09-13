# 利用排序，使得y按照逆序排序
# 但是在valid y的值的时候，需要升序值，则x必然增加，形成了齿型结构


from typing import List, Tuple, Optional
from math import inf 
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))  # x 升序，y 降序
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for (_, y2) in points[i + 1:]:
                if y1 >= y2 > max_y:
                    max_y = y2
                    ans += 1
                if max_y == y1:  # 优化
                    break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-number-of-ways-to-place-people-ii/solutions/2630655/on2-you-ya-mei-ju-by-endlesscheng-z86d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。