# https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/
from typing import List, Tuple, Optional


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        check_list = list(range(n - 1))

        ans = 0
        for j in range(m):
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    # j 列不是升序，必须删
                    ans += 1
                    break
            else:
                # j 列是升序，不删更好
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        # 相邻字母相等，下一列 i 和 i+1 需要继续比大小
                        check_list[new_size] = i  # 原地覆盖
                        new_size += 1
                del check_list[new_size:]
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/solutions/3854437/cong-zuo-dao-you-tan-xin-you-hua-pythonj-67o1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。