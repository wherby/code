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

def multiply(mata,matb,mod =10**9+7):
    return [[sum(x * y for x, y in zip(row, col)) % mod for col in zip(*matb)]
            for row in mata]


def vecmul(v,mat,mod =10**9+7):
    n = len(v)
    w = [0]*n
    for i in range(n):
        vi = v[i]
        if vi:
            Ai = mat[i]
            for j in range(n):
                w[j] = (w[j] + vi * Ai[j]) % mod
    return w


## Will Timeout https://leetcode.com/problems/number-of-zigzag-arrays-ii/submissions/1784912546/
def multiply2(mat1,mat2,mod =10**9+7):
    n = len(mat1)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
            for j in range(n):
                for k in range(n):
                    res[i][j] += mat1[i][k] *mat2[k][j]
                    res[i][j] %= mod
    return res