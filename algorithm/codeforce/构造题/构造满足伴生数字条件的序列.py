# https://codeforces.com/problemset/problem/145/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0902/solution/cf145b.md
# 构造序列满足 4,7,47,74 的个数满足的序列
# 因为47，74 条件比4,7 严格，所以首先构造
# 4444444777774444477   这样一个47和 74 是伴生的，所以序列只差一个
# 用 47 和 74 先构建基础，然后把其他的插入


import init_setting
from lib.cflibs import *
def main():
    c4, c7, c47, c74 = MII()
    
    if abs(c47 - c74) > 1: print(-1)
    else:
        if c47 - c74 == 1 or (c47 == c74 and c4 >= c47 + 1 and c7 >= c47):
            ans = [4, 7] * c47
            if c47 == c74: ans.append(4)
        else:
            ans = [7, 4] * c74
            if c47 == c74: ans.append(7)
    
        c4 -= ans.count(4)
        c7 -= ans.count(7)
        if c4 >= 0 and c7 >= 0:
            res = []
            
            for x in ans:
                if x == 4:
                    while c4:
                        c4 -= 1
                        res.append(4)
                res.append(x)
            
            if res[-1] == 7:
                for x in range(c7):
                    res.append(7)
            else:
                res.pop()
                for x in range(c7):
                    res.append(7)
                res.append(4)
            
            print(''.join(map(str, res)))
        else:
            print(-1)