#作者：小羊肖恩
#链接：https://leetcode.cn/circle/discuss/qSroZL/view/pqQGdQ/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        if self.find(b) != self.find(a):
            self.size[self.find(a)] += self.size[self.find(b)]
            self.parent[self.find(b)] = self.find(a)

    def getSize(self, a):
        return self.size[self.find(a)]

