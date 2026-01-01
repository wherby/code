import sys,os
parent_directory_concise= os.path.dirname(os.path.abspath(__file__))
for i in range(1):
    parent_directory_concise = os.path.dirname(parent_directory_concise)
sys.path.append(parent_directory_concise)
print(parent_directory_concise)

from quick_pow import *
mod =10**9+7

a = [[1,1],[1,0]]
print(matrix_pow(a,2,mod-1))
print(matrix_pow(a,3,mod-1))
print(matrix_pow(a,4,mod-1))

# 斐波那契数列
# F[n+1] = F[n] + F[n-1]
# F[n]   = F[n] + 0* F[n-1]

# 所以矩阵表示是  [[1,1],[1,0]]

# 如果 其实项不是 1,2 而是 A，B
# A =5 ,B =3 为例，  5,3， 15， 45,675。。
# algorithm/quickPow/斐波那契/非正常开始的斐波那契数列.png
A,B =5,3
a = [[1,1],[1,0]]
a2 = matrix_pow(a,2,mod-1)
a3 = matrix_pow(a,3,mod-1)
a4 = matrix_pow(a,4,mod-1)

def getComb(a):
    global A,B
    return pow(A,a[1][1],mod)* pow(B,a[1][0],mod) %mod

print(getComb(matrix_pow(a,0,mod-1))) # 为了取得第一位，需要在0次幂上计算
print(getComb(a))
print(getComb(a2))
print(getComb(a3))
print(getComb(a4))

def getN(A,B,n):
    if n == 0:
        return A 
    return getN(B,A*B%mod,n-1)
print(getN(5,3,100),getComb(matrix_pow(a,100,mod-1)))


## 如果递推公式是 F[n]  = F[n-1]^m *F[n-2]^n 则a=[[m,n],[1,0]]
# algorithm/quickPow/斐波那契/pic/高阶递推.png algorithm/quickPow/斐波那契/pic/高阶递推2.png. algorithm/quickPow/斐波那契/pic/高阶递推3.png


