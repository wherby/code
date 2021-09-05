#https://www.codeproject.com/Tips/792255/Faulhaber-made-easy
def Simplify(a, b):
    # Divide a and b by their gcd
    c, d= a, b 
    while d != 0:
        c, d= d, c % d
    return (a / c, b / c)

def SAXPY(A, X, Y):
    # Compute A.X + Y, where A, X and Y are fractions
    S= Simplify(A[0] * X[0], A[1] * X[1])
    S= Simplify(S[0] * Y[1] + S[1] * Y[0], S[1] * Y[1])
    return S

def GetKthFaulhaber(K):
    # Apex
    Pascal= [[1]]
    # Rows
    for i in range(1, K + 2):
        Pascal.append([1])
        for j in range(1, i):
            # Recurrence relation
            Pascal[i].append(Pascal[i-1][j-1] + Pascal[i-1][j])
        Pascal[i].append(1)

    # Compute the Faulhaber polynomial
    for k in range(K + 1):
        # Initialize the leading coefficient
        S= [(1, k+1)]

        # Compute the next coefficients from the triangular system
        for i in range(k):
            T= (0, 1)
            for j in range(i + 1):
                # Accumulate, with alternating signs
                T= SAXPY(S[j], Simplify(Pascal[k + 1 - j][k - 1 - i], (i - k if (i + j) & 1 else k - i)), T)
            S.append(T)
    return S
print GetKthFaulhaber(10)