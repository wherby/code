# Not verified.
import random
import math


class DoubleHashPermutation:
    def __init__(self, arr: list[int]):
        """
        初始化时传入任意排列或数组 arr
        """
        self.p = list(arr)
        self.k = len(self.p)

        # 1. 确保基数 pw 严格大于当前数组中的最大元素值，防止进制坍缩
        max_val = max(self.p) if self.k > 0 else 0
        lower_bound = max(max_val + 100, 10**6)
        self.pw = random.randint(lower_bound, 2 * lower_bound)

        # 2. 生成与基数互质的双大模数
        def gen():
            while True:
                x = random.getrandbits(40)
                if math.gcd(x, self.pw) == 1:
                    return x

        self.rnd1 = gen()
        self.rnd2 = gen()

        # 3. 预处理两个模数下的幂次
        self.pw1 = [1] * (self.k + 1)
        self.pw2 = [1] * (self.k + 1)
        for i in range(self.k):
            self.pw1[i + 1] = (self.pw1[i] * self.pw) % self.rnd1
            self.pw2[i + 1] = (self.pw2[i] * self.pw) % self.rnd2

        # 4. 初始化前缀哈希数组（支持无逆元的区间查询）
        self.pref1 = [0] * (self.k + 1)
        self.pref2 = [0] * (self.k + 1)
        self._build_prefix_hashes()

    def _build_prefix_hashes(self):
        """构建/重建前缀哈希（参考无逆元 StringHash 的 Horner 展开）"""
        v1, v2 = 0, 0
        for i in range(self.k):
            v1 = (v1 * self.pw + self.p[i]) % self.rnd1
            v2 = (v2 * self.pw + self.p[i]) % self.rnd2
            self.pref1[i + 1] = v1
            self.pref2[i + 1] = v2

    def swap(self, x: int, y: int):
        """
        交换位置 x 和 y 的元素。
        注意：如果后续需要调用区间查询 `query`，交换后需要维护前缀哈希。
        """
        # 1. 实际交换元素
        self.p[x], self.p[y] = self.p[y], self.p[x]

        # 2. 重建前缀哈希（如果 k 很大且调用频繁，可优化为局部更新；若 k 适中直接重建最稳妥）
        self._build_prefix_hashes()

    def get_hash(self) -> tuple[int, int]:
        """获取当前整个序列的全局双哈希值"""
        return (self.pref1[self.k], self.pref2[self.k])

    def query(self, left: int, right: int) -> tuple[int, int]:
        """
        类似 StringHash 的无逆元区间查询：
        获取子区间 [left, right)（左闭右开）的双哈希值。
        无需求逆元，通过乘法对齐高位直接做差。
        """
        length = right - left
        h1 = (self.pref1[right] - self.pref1[left] * self.pw1[length]) % self.rnd1
        h2 = (self.pref2[right] - self.pref2[left] * self.pw2[length]) % self.rnd2
        return ((h1 + self.rnd1) % self.rnd1, (h2 + self.rnd2) % self.rnd2)
