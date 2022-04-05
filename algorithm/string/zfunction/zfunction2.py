#https://cp-algorithms.com/string/z-function.html
def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1,N):
        if i <= R:
            Z[i] = min(R-i+1,Z[i-L])
        else:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
    return Z

a = "aabxaabx"
za =calculate_z_array(a)
print(za)