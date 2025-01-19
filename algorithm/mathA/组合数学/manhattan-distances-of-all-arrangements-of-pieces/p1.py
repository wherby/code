# 预处理阶乘以及其逆元
max_n = int(1e5)
fac = [1] * (max_n+1)
facinv = [1] * (max_n+1)

MAX_NUM = int(1e9+7)
for i in range(1,max_n+1):
    fac[i] = fac[i-1] * i % MAX_NUM
    # python自带快速幂
    facinv[i] = pow(fac[i],MAX_NUM-2,MAX_NUM)


def myComb(n,m):    
    if m < 0 or n < m:
        return 0
    return fac[n] * facinv[m] * facinv[n-m] % MAX_NUM

# 两距离组合
def C(m,n):
    return myComb(m+n,n)
    
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        '''
        AB两个格子
        假设 A 有棋子，B有棋子有多少种情况？
        t = m * n
        C(t-2,k-2)
        等概率的思想，枚举A，其它点都有可能是B，且等概率，即情况数是一致的
        
        贡献法，求B点对A的贡献和
        列行贡献再拆分，计算完列再计算行
        '''
        res = 0   
        two = facinv[2]     
        for i in range(n):
            for j in range(m):                
                '''
                行贡献
                当前行向上，距离分别为
                0 1 2 3 4 i
                向下
                0 1 2 3 4 n-i-1
                每一行都有m个值，即
                0*m+1*m+2*m+...+i*m
                '''
                res += m*(0+i)*(i+1)*two
                res += m*(0+n-i-1)*(n-i)*two
                '''
                列贡献
                同上
                0 1 2 3 j
                0 1 2 3 m-j-1
                每列n个值
                '''                
                res += n*(0+j)*(j+1)*two
                res += n*(0+m-j-1)*(m-j)*two
                res %= MAX_NUM
                
        
        res *= myComb(m*n-2,k-2) * two
        
        return res % MAX_NUM

# 作者：mipha
# 链接：https://leetcode.cn/problems/manhattan-distances-of-all-arrangements-of-pieces/solutions/3051348/mei-ju-gong-xian-fa-zu-he-shu-xue-deng-g-3481/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。