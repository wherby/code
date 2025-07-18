# C(x+1,n+1)=C(x,n+1)+C(x,n)
# C(x,x)+ C(x,x+1) + C(x,x+2) + C(x,n) == C(x+1,n+1)
# 上面这个求和也可以表示为 n 个位置，加上最后一个停止位置，一共有n+1个位置可以选择，并且选择m个位置，在m个位置后再选一个停止位，就是m+1个位置，所以和的最终值表示为 : C(m+1,n+1) 
import sys,os
parent_directory_concise = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parent_directory_concise = os.path.dirname(parent_directory_concise)
sys.path.append(parent_directory_concise)



from codeforce.lib.combineWithPreCompute import Factorial

f = Factorial(10000)

def getMid(mid):
    acc =0 
    for a in range(mid,10000):
        acc += f.comb(a,mid)
    return acc

mid = 4
print(getMid(mid)%f.MOD)
print(f.comb(10000,mid+1))
