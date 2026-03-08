from typing import List, Tuple, Optional


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        mx = max(map(max, grid))
        ans = 0
        # 试填法：ans 的第 i 位能不能是 0？
        # 如果在每一行的能选的数字中，都存在第 i 位是 0 的数，那么 ans 的第 i 位可以是 0，否则必须是 1
        for i in range(mx.bit_length() - 1, -1, -1):
            mask = ans | ((1 << i) - 1)  # mask 低于 i 的比特位全是 1，表示 grid[i][j] 的低位是 0 还是 1 无所谓
            for row in grid:
                for x in row:
                    # x 的高于 i 的比特位，如果 ans 是 0，那么 x 的这一位必须也是 0
                    # x 的低于 i 的比特位，随意
                    # x 的第 i 个比特位，我们期望它是 0
                    if (x | mask) == mask:  # x 可以选，且第 i 位是 0
                        break
                else:  # 这一行的可选数字中，第 i 位全是 1
                    ans |= 1 << i  # ans 第 i 位必须是 1
                    break  # 填下一位
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-bitwise-or-from-grid/solutions/3910784/shi-tian-fa-pythonjavacgo-by-endlesschen-b3zh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。