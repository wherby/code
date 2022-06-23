from functools import reduce
class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        # 斜率公式换算为乘积
        def sign(p, q, r):
            return (p[0] - r[0])*(q[1] - r[1]) - (p[1] - r[1])*(q[0] - r[0])
        
        # 判断添加点 r 是否在前面两点连线的右边
        def check_valid(points, r):
            points.append(r)
            while len(points) >= 3 and sign(*points[-3:]) < 0:
                points.pop(-2)
            return points
        
        trees.sort(key = lambda p: (p[0], p[1]))
        lower = reduce(check_valid, trees, [])
        upper = reduce(check_valid, trees[::-1], [])
        return lower + list(filter(lambda p: p not in lower, upper))