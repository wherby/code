# 如果要的 M*N的组合数，可以使用预处理
MAX_E = 14
MAX_N =100000

# 预处理组合数
C = [[0] * (MAX_E + 1) for _ in range(MAX_N + MAX_E)]
for i in range(len(C)):
    C[i][0] = 1
    for j in range(1, min(i, MAX_E) + 1):
        C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-the-number-of-ideal-arrays/solutions/1659088/shu-lun-zu-he-shu-xue-zuo-fa-by-endlessc-iouh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。