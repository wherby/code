



class LazySegmentTree:
    """
    Reference
    https://github.com/atcoder/ac-library/blob/master/atcoder/lazysegtree.hpp
    https://github.com/atcoder/ac-library/blob/master/document_en/lazysegtree.md
    https://github.com/atcoder/ac-library/blob/master/document_ja/lazysegtree.md
    """
    def __init__(self, n, op, e, mapping, composition, id):
        self.n = n
        self.op = op
        self.e = e
        self.mapping = mapping
        self.composition = composition
        self.id = id
        self.log = (n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [e] * (2 * self.size)
        self.lz = [id] * (self.size)

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def all_apply(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        if self.lz[k] != self.id:
            self.all_apply(2 * k, self.lz[k])
            self.all_apply(2 * k + 1, self.lz[k])
            self.lz[k] = self.id

    def build(self, v):
        assert len(v) <= self.n
        for i in range(len(v)):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0 ,-1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p < self.n
        p += self.size
        for i in range(self.log, 0, -1):
            self.push(p >> i)
        return self.d[p]

    # return [l,r)
    def prod(self, l, r):
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r-1) >> i)
        sml = smr = self.e
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.d[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    # def apply(self, p, f):
    #     assert 0 <= p < self.n
    #     p += self.size
    #     for i in range(self.log, 0, -1):
    #         self.push(p >> i)
    #     self.d[p] = self.mapping(f, self.d[p])
    #     for i in range(1, self.log + 1):
    #         self.update(p >> i)
    
    # (2) It applies a[i] = f(a[i]) for all i = l..r-1.
    def apply(self, l, r, f):
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if (l >> i) << i != l:
                self.push(l >> i)
            if (r >> i) << i != r:
                self.push((r - 1) >> i)
        l2 = l
        r2 = r
        while l < r:
            if l & 1:
                self.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self.all_apply(r, f)
            l >>= 1
            r >>= 1
        l = l2
        r = r2
        for i in range(1, self.log + 1):
            if (l >> i) << i != l:
                self.update(l >> i)
            if (r >> i) << i != r:
                self.update((r - 1) >> i)

    # maxright: 从l 开始向右查询，找到第一个不符合g的
    def max_right(self, l, g):
        assert 0 <= l <= self.n
        assert g(self.e)
        #print(g,self.e)
        if l == self.n:
            return self.n
        l += self.size
        for i in range(self.log, 0, -1):
            self.push(l >> i)
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            #print(l,self.d[l],self.op(sm, self.d[l]))
            if not g(self.op(sm, self.d[l])):
                while l < self.size:
                    self.push(l)
                    l = 2 * l
                    if g(self.op(sm, self.d[l])):
                        sm = self.op(sm, self.d[l])
                        l += 1
                #print(sm)
                return l - self.size
            sm = self.op(sm, self.d[l])
            l += 1
            if (l & -l) == l:
                return self.n

    # 从r开始往左查询。查找最小符合g的l
    def min_left(self, r, g):
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        for i in range(self.log, 0, -1):
            self.push((r - 1) >> i)
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self.op(self.d[r], sm)):
                while r < self.size:
                    self.push(r)
                    r = 2 * r + 1
                    if g(self.op(self.d[r], sm)):
                        sm = self.op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.d[r], sm)
            #print(sm,"sm",self.d[r],r)
            if (r & -r) == r:
                return 0

mod = 10**9+7
def createMaxMinSegTree(arr)->LazySegmentTree:
    def max_min_op(x, y):
        # x = (max_pos, idx_pos, max_neg, idx_neg)
        # y = (max_pos_y, idx_pos_y, max_neg_y, idx_neg_y)
        
        # 聚合 V_POS: 比较 (value, index)
        if y[0] > x[0] or (y[0] == x[0] and y[1] < x[1]):
            new_max_pos, new_idx_pos = y[0], y[1]
        else:
            new_max_pos, new_idx_pos = x[0], x[1]
            
        # 聚合 V_NEG: 比较 (value, index)
        if y[2] > x[2] or (y[2] == x[2] and y[3] < x[3]):
            new_max_neg, new_idx_neg = y[2], y[3]
        else:
            new_max_neg, new_idx_neg = x[2], x[3]
            
        return (new_max_pos, new_idx_pos, new_max_neg, new_idx_neg)
    E = ( 0,0,0,0)
    # 3. mapping: 如何将懒标记 f (delta) 应用到数据 x (max, min)
    def max_min_mapping(f, x) :
        if f%2 == ID:  # 优化：如果懒标记是单位元，直接返回
            return x
        
        return (x[2], x[3], x[0], x[1])

    # 4. composition: 如何合并新的懒标记 f 和旧的懒标记 g
    def max_min_composition(f, g) :
        # 懒标记是可累加的 (new_delta + old_delta)
        return (f + g)%2
    ID=0
    max_min_tree = LazySegmentTree(
    n=len(arr),
    op=max_min_op,
    e=E,
    mapping=max_min_mapping,
    composition=max_min_composition,
    id=ID)
    arr = [(a,i,mod-a if a !=0 else 0,i) for i,a in enumerate(arr)]
    max_min_tree.build(arr)
    return max_min_tree


def resolve():
    n = int(input())
    ls = list(map(lambda x: int(x),input().split()))
    ls = [0]+ls
    cnt = 0
    m = int(input())
    mmst = createMaxMinSegTree(ls)
    for _ in range(m):
        l,r = list(map(lambda x: int(x),input().split()))
        mmst.apply(l,r+1,1)
        mx = mmst.prod(1,n)
        #print(mx,mmst.max_right(1,lambda x:x[0] < mx[0]))
        #print(mmst.all_prod())
        cnt += mmst.all_prod()[1]
    return cnt

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)