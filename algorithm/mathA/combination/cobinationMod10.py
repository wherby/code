# 求C(m,n)在mod 10下的值，需要把 2和5的元素分开算，然后其他值在10的值域下求逆元
# Only this will pass https://leetcode.cn/contest/weekly-contest-438/problems/check-if-digits-are-equal-in-string-after-operations-ii/submissions/
c2 = [0] * 100001
c5 = [0] * 100001
tmp = [1] * 100001

for i in range(1, 100001):
    x = i
    c2[i] = c2[i - 1]
    while x % 2 == 0:
        x //= 2
        c2[i] += 1
    c5[i] = c5[i - 1]
    while x % 5 == 0:
        x //= 5
        c5[i] += 1
    tmp[i] = tmp[i - 1] * x % 10

rev_tmp = [1] * 100001
rev_tmp[100000] = pow(tmp[100000], -1, 10)  # pow(x,-1,mod) 求 x 在mod的情况下的逆元？

for i in range(100000, 0, -1):
    x = i
    while x % 2 == 0:
        x //= 2
    while x % 5 == 0:
        x //= 5
    rev_tmp[i - 1] = rev_tmp[i] * x % 10

def c(x, y):
    ans = tmp[x] * rev_tmp[y] * rev_tmp[x - y] % 10
    v = c2[x] - c2[y] - c2[x - y]
    ans *= pow(2, v, 10)
    v = c5[x] - c5[y] - c5[x - y]
    ans *= pow(5, v, 10)
    return ans % 10

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(a) for a in s]
        s1,s2 = s[:-1],s[1:]
        n= len(s1)
        t = (n)//2
        ls1=[]
        for i in range(t):
            ls1.append((s1[i] + s1[-1-i] -s2[i]-s2[-1-i])%10)
            #print(i,ls1,s1[i] , s1[-1-i] ,s2[i],s2[-1-i])
        if n %2 ==1:
            ls1.append(s1[(n)//2] - s2[(n)//2])
        #print(ls1)
        acc = 0 
        for i,a in enumerate(ls1):
            if a !=0:
                acc += a*c(n-1,i)
        return acc %10 ==0

re =Solution().hasSameDigits("3902")
print(re)