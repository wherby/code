# https://cp-algorithms.com/string/z-function.html
# Use zfunction2 for concise  <+ wrong version
# this version correct
# Verified in https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/submissions/564938556/

def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and s[R - L] == s[R]:
                R += 1
            R -= 1
            Z[i] = R - L + 1
        else:
            k = i - L
            if Z[k] + i <= R:
                Z[i] = Z[k]
            else:
                L = i
                while R < N and s[R - L] == s[R]:
                    R += 1
                R -= 1
                Z[i] = R - L + 1
        #print(i,L,R,Z)
    return Z

a = "ccacc#cccaaaacba"
za =calculate_z_array(a)
print(za)