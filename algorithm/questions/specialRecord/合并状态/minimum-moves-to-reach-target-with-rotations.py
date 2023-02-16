# https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/

#本题相当于在网格图上求起点到终点的最短路长度，这可以用 BFS 解决。相比一般的网格图 BFS（例如 1926 题），本题多了个「水平／竖直状态」
# ，这可以通过添加一个维度来解决，也就是用 (x,y,s) 表示蛇尾在第 x 行第 y 列，s=0 表示水平状态，
# s=1表示竖直状态。这样初始位置为 (0,0,0)，最终位置为 (n-1,n-2,0)。

#一些同学在写代码时，会写出很多的 if-else，对这 6 种移动方式分别编程：

#水平状态：向下移动／向右移动／顺时针旋转 9090 度。
#竖直状态：向下移动／向右移动／逆时针旋转 9090 度。
#代码越长，就越容易出 bug。能否总结出这 6 种移动方式的异同，用同一份代码解决呢？

#无论是水平状态还是竖直状态：

#向下移动：x 增加 1，y 和 s 不变。用三元组 (1,0,0) 表示。
#向右移动：y 增加 1，x 和 s 不变。用三元组 (0,1,0) 表示。
#旋转：s 切换，即 0 变为 1，1 变为 0；x 和 y 不变。用三元组 (0,0,1) 表示。
#三元组中的数字表示 (x,y,s) 每个值对应的变化量。对于旋转可以用异或运算解决。

#这样就能把 6 种移动方式用 3 个三元组表示了。把这 3 个三元组存到数组 \textit{dirs}dirs 中，遍历 \textit{dirs}dirs，用同一份代码处理不同的移动，这样就不用对每种移动各写一份代码了。

#最后，还需要判断：

#移动后蛇身不能出界。
#移动后蛇身不能在障碍物上。
#对于旋转，还需要保证 (x+1,y+1)没有障碍物。
#蛇尾在 (x,y)，蛇头呢？如果 s=0，蛇头在 (x,y+1)；如果 s=1，蛇头在 (x+1,y)。也可以合并为一个公式表示蛇头：

#(x+s,y+(s\oplus 1))
#(x+s,y+(s⊕1))

#其中 \oplus⊕ 表示异或运算。

#作者：endlesscheng
#链接：https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/solution/huan-zai-if-elseyi-ge-xun-huan-chu-li-li-tw8b/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List, Tuple, Optional
class Solution:
    def minimumMoves(self, g: List[List[int]]) -> int:
        step, n = 1, len(g)
        vis = {(0, 0, 0)}
        q = [(0, 0, 0)]  # 初始位置
        while q:
            tmp = q
            q = []
            for X, Y, S in tmp:
                for t in (X + 1, Y, S), (X, Y + 1, S), (X, Y, S ^ 1):  # 直接把移动后的位置算出来
                    x, y, s = t
                    x2, y2 = x + s, y + (s ^ 1)  # 蛇头
                    if x2 < n and y2 < n and t not in vis and \
                       g[x][y] == 0 and g[x2][y2] == 0 and (s == S or g[x + 1][y + 1] == 0):
                        if x == n - 1 and y == n - 2:  # 此时蛇头一定在 (n-1,n-1)
                            return step
                        vis.add(t)
                        q.append(t)
            step += 1
        return -1
    