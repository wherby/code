
## 返回最低位为1 的权值
def lowbit(n):
    return n &(-n)

print(lowbit(15))

## 这是一个错误的实现，如果n最低位为1，则返回2，否则返回最低位为1 的 权值
def lowbit2(n):
    return n &(-n+1)

print(lowbit2(12))
print(lowbit2 (15))
print(lowbit2(11))