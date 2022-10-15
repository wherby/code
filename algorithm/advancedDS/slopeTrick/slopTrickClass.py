# https://leetcode.cn/problems/NfY1m5/solution/python-slopetrickkuang-jia-by-981377660l-c70y/
class Solution:
    def buildBridge(self, _num: int, wood: List[List[int]]) -> int:
        S = SlopeTrick()
        length = [b - a for a, b in wood]
        for i, (left, _) in enumerate(wood):
            S.addLeftOffset(-length[i])
            if i > 0:
                S.addRightOffset(length[i - 1]) 
            S.addAbsXMinusA(left)
        return S.getMinY()



INF = int(1e18)

class SlopeTrick:
    """
    https://maspypy.com/slope-trick-1-%e8%a7%a3%e8%aa%ac%e7%b7%a8

    上记の记事にもとづき、@caomeinaixiさんが実装したテンプレートです。
    """

    __slots__ = "_minY", "_leftTuring", "_rightTuring", "_leftOffset", "_rightOffset"

    def __init__(
        self, leftTuring: Optional[List[int]] = None, rightTuring: Optional[List[int]] = None
    ) -> None:
        self._minY = 0  # dp 最小値
        self._leftTuring = [INF] if leftTuring is None else leftTuring  # 左拐点
        self._rightTuring = [INF] if rightTuring is None else rightTuring  # 右拐点
        self._leftOffset = 0  # 左拐点的平移量
        self._rightOffset = 0  # 右拐点的平移量

    def addAbsXMinusA(self, a: int) -> None:
        """|x-a|の加算:O(logn) 时间"""
        self.addXMinusA(a)
        self.addAMinusX(a)

    def addXMinusA(self, a: int) -> None:
        """(x-a)+の加算:O(logn) 时间

        倾きの変化点に a が追加されます
        minYの変化はf(left0)に等しい
        """
        if len(self._leftTuring) != 0:
            self._minY += max(0, self.leftTop - a)
        self._pushLeft(a)
        self._pushRight(self._popLeft())

    def addAMinusX(self, a: int) -> None:
        """(a-x)+の加算:O(logn) 时间

        倾きの変化点に a が追加されます
        minYの変化はf(right0)に等しい
        """
        if len(self._rightTuring) != 0:
            self._minY += max(0, a - self.rightTop)
        self._pushRight(a)
        self._pushLeft(self._popRight())

    def addY(self, delta: int) -> None:
        """yの加算:O(1) 时间"""
        self._minY += delta

    def addOffset(self, delta: int) -> None:
        """平移:O(1) 时间

        g(x) = f(x - a)
        fをg に取り换える
        """
        self._leftOffset += delta
        self._rightOffset += delta

    def addLeftOffset(self, delta: int) -> None:
        """左拐点の平移:O(1) 时间"""
        self._leftOffset += delta

    def addRightOffset(self, delta: int) -> None:
        """右拐点の平移:O(1) 时间"""
        self._rightOffset += delta

    def updateLeftMin(self) -> None:
        """累积 min:O(1) 时间

        g(x) = min(f(y) | y <= x)
        fをg に取り换える

        rightTuringを空集合に取り换える
        """
        self._rightTuring = [INF]

    def updateRightMin(self) -> None:
        """累积 min:O(1) 时间

        g(x) = min(f(y) | y >= x)
        fをg に取り替える

        leftTuringを空集合に取り换える
        """
        self._leftTuring = [INF]

    def updateWindowMin(self, leftDiff: int, rightDiff: int) -> None:
        """累积 min:O(1) 时间

        g(x) = min(f(y) | `x - leftDiff <= y <= x - rightDiff`)
        fをg に取り替える

        左侧集合・右侧集合それぞれを平行移动する
        left0, right0 => left0 + rightDiff, right0 + leftDiff
        """
        self._leftOffset += rightDiff
        self._rightOffset += leftDiff

    def getMinY(self) -> int:
        """最小値の取得:O(1) 时间"""
        return self._minY

    def _pushLeft(self, a: int) -> None:
        heappush(self._leftTuring, -a + self._leftOffset)

    def _pushRight(self, a: int) -> None:
        heappush(self._rightTuring, a - self._rightOffset)

    def _popLeft(self) -> int:
        return -heappop(self._leftTuring) + self._leftOffset

    def _popRight(self) -> int:
        return heappop(self._rightTuring) + self._rightOffset

    @property
    def leftTop(self) -> int:
        """左侧の倾きの変化点の最大値left0の取得:O(1)时间"""
        return -self._leftTuring[0] + self._leftOffset

    @property
    def rightTop(self) -> int:
        """右侧の倾きの変化点の最小値right0の取得:O(1)时间"""
        return self._rightTuring[0] + self._rightOffset

