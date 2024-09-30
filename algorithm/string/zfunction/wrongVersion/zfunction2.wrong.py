#https://cp-algorithms.com/string/z-function.html 
# Wrong version Don't use
# To be versified in  https://leetcode.cn/contest/weekly-contest-415/problems/minimum-number-of-valid-strings-to-form-target-ii/submissions/564938556/
# contest/00000c397d130/c415/q4/t4.py
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
a = "aaabaab"
za =calculate_z_array(a)
a = "ccacc#cccaaaacba" # wrong answer
za =calculate_z_array(a)
print(za)