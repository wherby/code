# https://codeforces.com/gym/102861/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0915/solution/cf102861k.md

# 因为只有联通分量为偶数的时候，图才是可分的，所以
# 当cnt[i] 时候，这时候 i 有奇数个点，所以把 neighbor[i] |= 1 << i + 1， 奇数+1 = 偶数个元素
# else: neighbor[i] |= 1 这咯把最后一位(等号右边的常数项) 置1 ，右边也是偶数个元素
# 所以产生的消元变量也是偶数个系数
# check(1) 的时候，验证，所有基向量 和 0000000001正交

# 在线性代数中：
# 方程组有解 ⇔ 增广矩阵的秩等于系数矩阵的秩
# 出现 0 = 1 的方程 ⇔ 增广矩阵的秩 > 系数矩阵的秩
# check(1) 正是在检查是否存在这样的秩不一致情况

# 6. 在图划分问题中的具体表现
# 对于连通分量大小为奇数的图：
# 总会出现 rank([A|b]) = rank(A) + 1
# 多出的这一个秩就对应着 0 = 1 的矛盾方程
# 因此 base.check(1) 返回 True
# 对于连通分量大小为偶数的图：
# rank([A|b]) = rank(A)
# 没有矛盾方程
# base.check(1) 返回 False

import init_setting
from cflibs import *
from lib.XorBasis import * 

def main():
    n, m = MII()
    base = XorBasis(n+1)
    
    neighbor = [0] * n
    cnt = [0] * n
    
    for _ in range(m):
        u, v = GMI()
        neighbor[u] |= 1 << v + 1
        neighbor[v] |= 1 << u + 1
        cnt[u] ^= 1
        cnt[v] ^= 1
    
    for i in range(n):
        if cnt[i]: neighbor[i] |= 1 << i + 1
        else: neighbor[i] |= 1
    
    for x in neighbor:
        base.insert(x)
    
    print('N' if base.check(1) else 'Y')

main()