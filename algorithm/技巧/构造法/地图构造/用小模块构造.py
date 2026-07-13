# https://leetcode.cn/contest/weekly-contest-510/problems/create-grid-with-exactly-k-paths-i/
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        maps = {
            1: [(1, 1, ["."])],
            2: [(2, 2, ["..", ".."])],
            3: [
                (2, 3, ["...", "..."]),
                (3, 2, ["..", "..", ".."])
            ],
            4: [
                (2, 4, ["....", "...."]),
                (4, 2, ["..", "..", "..", ".."]),
                (3, 3, ["..#", "...", "#.."])
            ]
        }

        if k not in maps:
            return []

        for tm, tn, grid_t in maps[k]:
            if tm <= m and tn <= n:
               
                grid = [['#'] * n for _ in range(m)]

                
                for i in range(tm):
                    for j in range(tn):
                        grid[i][j] = grid_t[i][j]

                if tn < n:
                    for j in range(tn, n):
                        grid[tm - 1][j] = '.'
                
                if tm < m:
                    for i in range(tm, m):
                        grid[i][n - 1] = '.'

                return [''.join(row) for row in grid]

        return []