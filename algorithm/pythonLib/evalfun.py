# https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval("*".join(str(n))) - eval("+".join(str(n))) 