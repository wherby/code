
import numpy as np

MOD = 1_000_000_007

# a^n @ f0
def pow(a: np.ndarray, n: int, f0: np.ndarray) -> np.ndarray:
    res = f0
    while n:
        if n & 1:
            res = a @ res % MOD
        a = a @ a % MOD
        n >>= 1
    return res

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        pow3 = [3 ** i for i in range(m)]
        valid = []
        for color in range(3 ** m):
            for i in range(1, m):
                if color // pow3[i] % 3 == color // pow3[i - 1] % 3:  # 相邻颜色相同
                    break
            else:  # 没有中途 break，合法
                valid.append(color)

        nv = len(valid)
        m = np.zeros((nv, nv), dtype=object)
        for i, color1 in enumerate(valid):
            for j, color2 in enumerate(valid):
                for p3 in pow3:
                    if color1 // p3 % 3 == color2 // p3 % 3:  # 相邻颜色相同
                        break
                else:  # 没有中途 break，合法
                    m[i, j] = 1

        f0 = np.ones((nv,), dtype=object)
        res = pow(m, n - 1, f0)
        return np.sum(res) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/solutions/869703/zhuang-ya-dp-yu-chu-li-he-fa-zhuang-tai-l927s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。