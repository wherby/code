
# 使用pow(self.fac[-1],-1,self.mod) 求出阶乘的逆元，再一次求低阶阶乘的逆元
algorithm/mathA/combination.fast.py
这里只有乘法和两个值需要维护

algorithm/mathA/combineWithPreCompute.py ：这里有各种combination的函数


# 使用combination性质递归求值，速度慢，递归容易stack overflow
algorithm/mathA/combination.slowAndOverflow.py

# 使用逆元来递归求阶乘逆元， 这里多维护了一个逆元的变量和N次逆元计算
algorithm/mathA/combinationOthers.py
