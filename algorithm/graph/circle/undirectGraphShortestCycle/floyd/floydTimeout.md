# 如果用floyd 会timeout,因为是N**3复杂度 需要用[algorithm/graph/circle/undirectGraphShortestCycle/bfsSearchCycle.py] 来计算cycle，是N**2复杂度

## Issue

用floyd检测的时候，把dis作为外部变量在重复调用的时候会更改dis的值[algorithm/graph/circle/undirectGraphShortestCycle/floyd/floyd1.py] 

dis 需要放在 floyd函数里面重新赋值[algorithm/graph/circle/undirectGraphShortestCycle/floyd/floyd2.py]