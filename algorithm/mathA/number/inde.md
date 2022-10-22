# 


## get all number less than N


## 数位DP
https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/zui-da-wei-n-de-shu-zi-zu-he-by-leetcode-f3yi/

https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/shu-wei-dp-tong-yong-mo-ban-xiang-xi-zhu-e5dg/

```python
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s): return int(is_num)  # 如果填了数字，则为 1 种合法方案
            res = 0
            if not is_num:  # 前面不填数字，那么可以跳过当前数位，也不填数字
                # is_limit 改为 False，因为没有填数字，位数都比 n 要短，自然不会受到 n 的约束
                # is_num 仍然为 False，因为没有填任何数字
                res = f(i + 1, False, False)
            up = s[i] if is_limit else '9'  # 根据是否受到约束，决定可以填的数字的上限
            # 注意：对于一般的题目而言，如果此时 is_num 为 False，则必须从 1 开始枚举，由于本题 digits 没有 0，所以无需处理这种情况
            for d in digits:  # 枚举要填入的数字 d
                if d > up: break  # d 超过上限，由于 digits 是有序的，后面的 d 都会超过上限，故退出循环
                # is_limit：如果当前受到 n 的约束，且填的数字等于上限，那么后面仍然会受到 n 的约束
                # is_num 为 True，因为填了数字
                res += f(i + 1, is_limit and d == up, True)
            return res
        return f(0, True, False)

作者：endlesscheng
链接：https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/solution/shu-wei-dp-tong-yong-mo-ban-xiang-xi-zhu-e5dg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

https://github.com/EndlessCheng/codeforces-go/blob/master/copypasta/dp.go