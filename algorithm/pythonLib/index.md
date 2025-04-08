

# 初始化多维数组
arr = [[[0]*10 for _ in range(10) ] for _ in range(10)]


# maximum recursion depth exceeded while calling a Python object
在mac 中3.12版本不能work，3.9.6可以  https://wherby.github.io/docs/python/recursion/index.html

import sys
sys.setrecursionlimit(10**4)


## If-Else 特殊用法

algorithm/codeforce-etcs/BFS最短路.py

# 代码结构
```python
for x in range(10):
    if cnt[x] and dis[x] == 10:
        break
    res += cnt[x] * dis[x]
else:
    ans[i][j] = res
```
# 关键点解析
# for-else 结构：

# else 子句会在循环正常完成（即没有被 break 中断）时执行。

# 如果循环被 break 中断，else 部分不会执行。