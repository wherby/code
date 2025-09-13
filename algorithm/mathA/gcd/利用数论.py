# 利用欧拉函数和gcd的关系
#  algorithm/mathA/gcd/pic/1.png -- algorithm/mathA/gcd/pic/6.png
# 利用莫比乌斯反演， phi_arr[d] * total_count 本来应该是 d*(total_count - f(nd))[2<=n<M//d] 的容斥原理，但是用了 phi_arr 函数使得计算值总数是相等的
# 假设 d =12 (1,2,3,4,6,12)是它的除数因子   phi(1) + phi(2)+phi(3)+phi(4)+phi(6)+phi(12) = 12
# 对于循环条件为 12而言 total_count 里其实已经包含了GCD为 12*K 的子数组， 而没有包含 1,2,3,4,6 的子数组； 但是循环在1的时候，会包含GCD是12 的子数字，同理循环在2的时候也会包含gcd是12的子数组
from typing import List, Tuple, Optional

from collections import defaultdict

M_val = 70000

class Solution:
    precomputed = False
    phi_g = None
    divisors_g = None

    def totalBeauty(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        M = M_val
        if not Solution.precomputed:
            phi = list(range(M + 1))
            for i in range(2, M + 1):
                if phi[i] == i:
                    for j in range(i, M + 1, i):
                        phi[j] -= phi[j] // i
            Solution.phi_g = phi

            divisors = [[] for _ in range(M + 1)]
            for i in range(1, M + 1):
                for j in range(i, M + 1, i):
                    divisors[j].append(i)
            Solution.divisors_g = divisors
            Solution.precomputed = True

        phi_arr = Solution.phi_g
        divisors_arr = Solution.divisors_g

        arr_by_d = defaultdict(list)
        divisors_appear = set()
        for x in nums:
            for d in divisors_arr[x]:
                if d <= M:
                    arr_by_d[d].append(x)
                    divisors_appear.add(d)
        
        ans = 0
        for d in divisors_appear:
            L = arr_by_d[d]
            if not L:
                continue
            distinct_vals = sorted(set(L))
            comp = {val: idx + 1 for idx, val in enumerate(distinct_vals)}
            n_comp = len(distinct_vals)
            fenw = [0] * (n_comp + 1)
            total_count = 0
            for x in L:
                pos = comp[x]
                s = 0
                idx = pos - 1
                while idx > 0:
                    s = (s + fenw[idx]) % mod
                    idx -= idx & -idx
                count_here = (1 + s) % mod
                total_count = (total_count + count_here) % mod
                idx = pos
                while idx <= n_comp:
                    fenw[idx] = (fenw[idx] + count_here) % mod
                    idx += idx & -idx
            ans = (ans + phi_arr[d] * total_count) % mod
        return ans % mod