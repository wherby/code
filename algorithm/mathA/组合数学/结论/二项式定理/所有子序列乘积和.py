# 所有子序列乘积可以用二项式定理证明 等于 (1+ai)的乘积

ls = [1,2,3,4,5,6]

def getSubSeqProdSum(ls):
    n = len(ls)
    sm = 0 
    for i in range(0,1<<n):
        acc = 1 
        for j in range(n):
            if (1<<j)& i :
                acc *= ls[j]
        sm += acc 
    return sm 

dsm = 1 
for i in ls :
    dsm *=(1+i )

print(dsm, getSubSeqProdSum(ls))
