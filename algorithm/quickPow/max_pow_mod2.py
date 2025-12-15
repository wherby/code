
def matrix_mul(A, B, N):
    """
    计算 A * B 模 2 的结果 (使用 XOR 和 AND 运算)
    N 是矩阵的维度 (N*N)
    """
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            sum_val = 0
            # 模 2 矩阵乘法： A[i][k] * B[k][j] 的和
            for k in range(N):
                # 乘法是 AND (逻辑与)
                product = A[i][k] & B[k][j] 
                # 加法是 XOR (异或)
                sum_val ^= product
            
            C[i][j] = sum_val
            
    return C

def matrix_pow(A, k):
    """
    计算 A 的 k 次方，模 2 意义下
    A 是方阵
    k 是指数
    """
    N = len(A)
    
    # 结果矩阵 R 初始化为单位矩阵 I
    R = [[0] * N for _ in range(N)]
    for i in range(N):
        R[i][i] = 1

    Base = A # Base 是当前需要乘的底数 (A, A^2, A^4, ...)
    power = k
    
    # 标准的矩阵快速幂算法
    while power > 0:
        # 如果当前 power 的最低位是 1
        if power & 1:
            # R = R * Base
            R = matrix_mul(R, Base, N)
        
        # Base = Base * Base (Base^2)
        Base = matrix_mul(Base, Base, N)
        
        # power = power // 2
        power >>= 1
        
    return R