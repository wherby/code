def quickPow(mat,k):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        res[i][i] =1 
    cur = [list(mat[i]) for i in range(n)]
    while k :
        if k %2 ==1:
            res = multiply(res,cur)
        k = k //2
        cur = multiply(cur,cur)
    return res

def multiply(mat1,mat2,mod =10**9+7):
    n = len(mat1)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += mat1[i][k] *mat2[k][j]
                    res[i][j] %= mod
    return res