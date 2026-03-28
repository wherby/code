# https://codeforces.com/gym/102154/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0324/solution/cf102154c.md
# 如果是正向操作的时候，操作的距离会以二分的情况减少，这样会引入以个LoGN的常数量，因为操作的结果最多是当前距离减半向左移动
# 但是如果是逆向操作，操作就变成了可以选择一个v作为操作距离的右移操作，因为可以使得被操作数在偶数的最后一个位置，则增加了v
# ，这样的操作数量是常数级别的，虽然如果被操作数是在index =1 的情况是 logN 的操作，但是这个位置只有1个数字，而且用randon的方式可以避免这个位置的数是原操作数
# 用了逆序的思路，如果需要排序，则等于用排好序的队列到原始数组位置的操作的逆序。使用了操作逆序反向操作，得到等价的变换
# 因为正向操作的时候，已经排序的左边界L 会使得操作增益最大是 (idx-L)//2
# 而逆向操作的时候，已经排序的是右边界L。则，很容易构造得到增益是（R-idx)的操作，只要当前idx 能在（R-idx)*2的前半部分的最后一个位置即可



import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    perm = LGMI()
    
    ops = []
    help_perm = list(range(n))
    
    def op(l, r):
        ops.append(f'{l + 1} {r + 1}')
        half = (r - l + 1) // 2
        vals = []
        for i in range(half):
            vals.append(help_perm[l + i + half])
            vals.append(help_perm[l + i])
        for i in range(l, r + 1):
            help_perm[i] = vals[i - l]
    
    for _ in range(500):
        l = random.randint(0, n - 1)
        r = random.randint(0, n - 1)
        
        if (r - l) % 2:
            if l > r: l, r = r, l
            op(l, r)
    
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if help_perm[j] == perm[i]:
                cur = j
                while cur != i:
                    v = fmin(cur + 1, i - cur)
                    op(cur - v + 1, cur + v)
                    cur += v
    
    ops.reverse()
    
    print(len(ops))
    print('\n'.join(ops))