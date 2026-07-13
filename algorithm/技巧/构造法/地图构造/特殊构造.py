# algorithm/技巧/构造法/地图构造/二进制构造.png 
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        # 特判
        if k == 4 and m == 3 and n == 3:
            return ["..#", "...", "#.."]

        if m == 1 or n == 1:
            # 单行或单列，只能有一种方案
            if k > 1:
                return []
            return ['.' * n] * m

        # 至少要有 k 行或 k 列（特殊情况上面已判断）
        if m < k and n < k:
            return []

        # 初始全为 '#'
        a = [['#'] * n for _ in range(m)]

        if m >= k:  # 至少有 k 行
            # 第一列改成 '.'
            for row in a:
                row[0] = '.'

            # 第二列末尾 k 个 '.'
            for i in range(m - k, m):
                a[i][1] = '.'

            # 最后一行改成 '.'
            a[-1] = ['.'] * n

        else:  # 至少有 k 列
            # 第一行改成 '.'
            a[0] = ['.'] * n

            # 第二行末尾 k 个 '.'
            for j in range(n - k, n):
                a[1][j] = '.'

            # 最后一列改成 '.'
            for row in a:
                row[-1] = '.'

        return [''.join(row) for row in a]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/create-grid-with-exactly-k-paths-i/solutions/3995102/gou-zao-ti-fu-geng-da-shu-ju-fan-wei-de-k4ebh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。