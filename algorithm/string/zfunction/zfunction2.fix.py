#https://cp-algorithms.com/string/z-function.html 
# fixed version
# Verified in https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/submissions/564938286/


def calculate_z_array(s):
    N = len(s)
    Z = [0] * N
    L, R = 0, 0
    for i in range(1,N):
        if i < R:
            Z[i] = min(R-i,Z[i-L])

        while i+ Z[i]< N and s[Z[i]]  == s[i+ Z[i]]:
            Z[i] +=1
        if i + Z[i]>R:
            L = i 
            R = i +Z[i] 
    return Z

a = "aabxaabx"
a = "aaabaab"
za =calculate_z_array(a)
a = "ccacc#cccaaaacba" # wrong answer
za =calculate_z_array(a)
print(za)