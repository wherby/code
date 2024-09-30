

# 初始化多维数组
arr = [[[0]*10 for _ in range(10) ] for _ in range(10)]


# maximum recursion depth exceeded while calling a Python object
在mac 中3.12版本不能work，3.9.6可以  https://wherby.github.io/docs/python/recursion/index.html

import sys
sys.setrecursionlimit(10**4)