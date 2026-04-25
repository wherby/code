# https://leetcode.cn/problems/good-subsequence-queries/description/
# 假设这个题目是从子序列改为子数组？这样实现对的吗？

import typing
import math

# 标准 GCD 函数
def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def _ceil_pow2(n: int) -> int:
    if n <= 1: return 0
    return (n - 1).bit_length()

class SegTree:
    def __init__(self,
                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],
                 e: typing.Any,
                 v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def all_prod(self) -> typing.Any:
        return self._d[1]

# --- 业务逻辑：处理好子数组 ---

def solve():
    # 假设输入
    n = 5
    p_target = 2
    nums = [4, 8, 2, 8, 4]
    queries = [[0, 2], [2, 10]] # [index, value]
    
    # 题目要求的中间变量
    norqaveliq = queries 

    # 节点定义: (total_gcd, prefix_list, suffix_list, has_good, length)
    # list 元素格式: [gcd_val, count]
    
    def make_leaf(val):
        # 单个元素长度为 1。如果 1 < n 且 val == p，则它是好子数组
        # 注意：这里的 1 < n 需要在 op 中感知，或者初始化时处理
        is_good = (val == p_target and n > 1)
        return (val, [[val, 1]], [[val, 1]], is_good, 1)

    def merge_op(l, r):
        # 处理单位元 e
        if l is None: return r
        if r is None: return l
        
        l_gcd, l_pre, l_suf, l_good, l_len = l
        r_gcd, r_pre, r_suf, r_good, r_len = r
        
        res_len = l_len + r_len
        res_gcd = get_gcd(l_gcd, r_gcd)
        
        # 1. 合并前缀 GCD 列表
        res_pre = [item[:] for item in l_pre]
        for g, cnt in r_pre:
            new_g = get_gcd(l_gcd, g)
            if new_g == res_pre[-1][0]:
                res_pre[-1][1] += cnt
            else:
                res_pre.append([new_g, cnt])
        
        # 2. 合并后缀 GCD 列表
        res_suf = [item[:] for item in r_suf]
        for g, cnt in l_suf:
            new_g = get_gcd(r_gcd, g)
            if new_g == res_suf[-1][0]:
                res_suf[-1][1] += cnt
            else:
                res_suf.append([new_g, cnt])
        
        # 3. 判定好子数组 (长度 < n 且 GCD == p)
        # 继承自子节点的结果
        res_good = l_good or r_good
        
        if not res_good:
            # 检查横跨左右边界的子数组
            # 使用双指针或暴力合并端点 GCD (由于列表长度极短，此处暴力合并)
            curr_l_len = 0
            for lg, l_cnt in l_suf:
                curr_l_len += l_cnt
                curr_r_len = 0
                for rg, r_cnt in r_pre:
                    curr_r_len += r_cnt
                    if get_gcd(lg, rg) == p_target:
                        # 核心判定：长度必须严格小于总长度 n
                        if curr_l_len + curr_r_len < n:
                            res_good = True
                            break
                    if res_good: break
                if res_good: break
        
        return (res_gcd, res_pre, res_suf, res_good, res_len)

    # 初始化线段树
    initial_data = [make_leaf(x) for x in nums]
    st = SegTree(op=merge_op, e=None, v=initial_data)

    results_count = 0
    for idx, val in norqaveliq:
        st.set(idx, make_leaf(val))
        if st.all_prod()[3]: # 索引 3 是 res_good
            results_count += 1
            
    return results_count

# 执行
print(f"满足条件的查询次数: {solve()}")