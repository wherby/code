# https://codeforces.com/gym/105813/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0121/solution/cf105813m.md
# 使用数字轮机构造MEX 问题
# 在每位数字上使用了双层填充的方法(据说可以增加鲁棒性？？)，然后增加目标值的方式，最后把目标值的最后一位弹出，导致目标数字不能生成
# 如果单层轮机的时候，要得到115，但是在105的时候可能构造不出？ 
# 1. 构造单层序列 $n$根据你的逻辑，每一段都是 [除c外的digits] + c。第 1 段 ($c=1$): [2, 3, 4, 5, 6, 7, 8, 9, 0] + 1
# 第 2 段 ($c=1$): [2, 3, 4, 5, 6, 7, 8, 9, 0] + 1
# 第 3 段 ($c=5$): [1, 2, 3, 4, 6, 7, 8, 9, 0] + 5 
# (最后这个 5 被 pop 掉了)完整的 $n$ 为：2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 6, 7, 8, 9, 0

#双层填充的本质是：它不在乎你的 digits 怎么排，也不在乎你的匹配指针跳到了段落的哪个位置。它保证在任何一个 $c$ 出现之前，所有的数字都至少有一次“保底”的出现机会。
# 总结单层构造：必须配合极其精密的排序算法，甚至可能需要根据 $s$ 的内容动态调整每一段的 digits 顺序，极其容易出错。
# 双层构造：通过冗余实现了“免疫排序”。无论你把 $0$ 放最后还是放最前，它都能保证 $105$ 一定会出现。


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    for _ in range(t):
        s = [int(c) for c in I()]
        ans = []
        
        for c in s:
            for _ in range(2):
                for x in digits:
                    if x != c:
                        ans.append(x)
            ans.append(c)
        
        ans.pop()
        outs.append(''.join(map(str, ans)))
    
    print('\n'.join(outs))