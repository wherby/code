# https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/

# 从答案出发倒着思考。关注最后全为 
# 0
# 0 或者全为 
# 1
# 1 的行，倒数第二步是什么样的？

# 假如翻转最后一列，
# 000
# 000 变成 
# 001
# 001，
# 111
# 111 变成 
# 110
# 110。从这个例子可以发现，对于相同的行，或者「互补」的行，一定存在一种翻转方式，可以使这些行最终全为 
# 0
# 0 或者全为 
# 1
# 1。

# 从图论的角度来看的话，就是在这些相同或者互补的行之间连边，答案就是最大连通块的大小。

# 但实际上不需要建图，用哈希表统计这些行。为了统计互补的行，可以把第一个数为 
# 1
# 1 的行全部翻转。

# 例如示例 3，把最后一行翻转得到 
# 001
# 001（变成互补的行），发现与第二行是一样的，所以答案等于 
# 2
# 2。

# 具体到代码，不同语言有着不同的实现方式：

# Python 直接转成 tuple 放入哈希表中。
# C++ 和 Java 转成字符串。
# Go 把每一行压缩到一个长为 
# ⌈
# 300
# /
# 64
# ⌉
# =
# 5
# ⌈300/64⌉=5 的 uint64 数组中。

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/solution/ni-xiang-si-wei-pythonjavacgo-by-endless-915k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dic = defaultdict(int)
        for row in matrix:
            if row[0] == 1 :
                row = [i^1 for i in row]
            dic[tuple(row)] +=1
        return max(dic.values())