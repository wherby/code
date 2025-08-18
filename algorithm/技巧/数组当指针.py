# https://codeforces.com/problemset/problem/518/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0816/solution/cf518c.md
# cur 开始是排列出现的顺序， 加上pos数组的辅助， cur[pos[i]]表示 i在 cur 数组的位置上的数字，就是i 了， 但是有了pos数组辅助，则可以很方便得到任意数字的左后数字是什么 cur[pos[i] +-1] 这时候 pos[i] 表达的是i 在数组的位置
# 可以当做指针使用。。

import init_setting
from codeforce.lib.cflibs import *
def main():
    n, m, k = MII()
    cur = LGMI()
    pos = [0] * n
    
    for i in range(n):
        pos[cur[i]] = i
    
    ans = 0
    for i in GMI():
        ans += pos[i] // k + 1
        
        if pos[i]:
            p = pos[i]
            pos[cur[p]], pos[cur[p - 1]] = pos[cur[p - 1]], pos[cur[p]] # 把记录位子的数组更新到交换后的位置， cur[p] 是i 对应的位子 cur[p-1]表示 i对应位置前一个数字的值
            cur[p], cur[p - 1] = cur[p - 1], cur[p]                 # 更新原数组的数字
    
    print(ans)

cur = [2, 0, 4, 1, 3]
print(cur)
pos = [0]*len(cur)
for i in range(len(cur)):
    pos[cur[i]] = i 
print(pos)
for i in range(len(cur)):
    print(i, cur[pos[i]])