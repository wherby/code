# 假设有N个格子，有k种颜色，用这些颜色染色，求x种颜色染色的方案数
#
# dp[i][j] 表示i个格子用j种元素染色
# 转移方程如果从小往大推则推不出来，只能从大往小推
# dp[i+1][j+1] = dp[i][j] + (j+1)*dp[i][j+1] 表示有两种情况，如果i个格子只有j种颜色，第i+1个格子只能选择第j+1种颜色， 如果i个格子已经有j+1种颜色，则i+1个格子可以选择j+1中任一颜色
# 如果要得到最终答案，还需要乘comb(k,x)*k! 
import sys,os
parent_directory_concise =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_directory_concise)

from lib.combineWithPreCompute import *
mod = 10**9+7

def getDP(n):
    dp= [0]*(n+1)
    dp[0] =1 

    for i in range(1,n+1):
        for j in range(i,0,-1):
            dp[j] = (dp[j-1] + j*dp[j]) %mod
        dp[0] =0
    return dp

def getCombOfX(n,k,x):
    fac = Factorial(10 ** 6, mod)
    dp = getDP(n)
    ret = dp[x]*fac.comb(k,x) *fac.fact(x)
    return ret

print(getCombOfX(2,10,1)) 
print(getCombOfX(2,10,2)) 
print(getCombOfX(3,10,2)) 
print(getCombOfX(10,2,2)) 