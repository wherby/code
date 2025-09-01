def getAllDivN(MAX):
    MAX = MAX +1
    fac = [[] for _ in range(MAX)]
    for i in range(1,MAX):
        for j in range(i,MAX,i):
            fac[j].append(i)
    return fac 
fac2 = getAllDivN(20001)
print(fac2[:20])


def getAllDividerReverse(MAX):
    MAX = MAX +1
    fac= [[] for _ in range(MAX)]
    for i in range(1,MAX):
        for j in range(i,MAX,i):
            fac[i].append(j)
    return fac

fac = getAllDividerReverse(50)
print(fac[:20])






# 预处理每个数的因子
MX = 70_001
divisors = [[] for _ in range(MX)]
for i in range(1, MX):
    for j in range(i, MX, i):
        divisors[j].append(i)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/sum-of-beautiful-subsequences/solutions/3768197/bei-shu-rong-chi-zhi-yu-shu-zhuang-shu-z-rs5w/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。