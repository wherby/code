
# total =digital_cnt -(j-c) 表示了，要构建digital_cnt 个数字，已经有了j-c 个位置已经插入数字， 剩下的可以插入数字的位置，
# if i == 0:total -=1,如果插入的数字是0，则除了第一个位置，其他位置都可以插入，所以要减去1
# 状态转移的时候用插入位置选取的方式考虑，则不用考虑最前面有多少个0的各种情况，如果插入0的时候，只用考虑不选取最高位就可以了。
# 可以看到 digital_cnt 不用考虑是否大于字符种类，如果小于的时候，一定dp[-1]==0

# 用枚举最终出现的数字位数的方式比生成数字dp的方式的考虑的状态转移方程更简单

import math

mod =10**9+7

def getValidCnt(ls):
    n = sum(ls)
    ans = 0

    for digital_cnt in range(1,n+1):
        dp = [0]*(digital_cnt+1)
        dp[0] =1

        for i in range(10):
            if ls[i]:
                ndp = [0]*(digital_cnt +1)
                for j in range(digital_cnt,0,-1):
                    for c in range(1,ls[i] +1):
                        if j -c < 0:break
                        total = digital_cnt -(j-c)
                        if i == 0:total -=1
                        if 0<=c<=total:
                            ndp[j] += dp[j-c] *math.comb(total,c)
                dp = ndp 
                #print("CX:",dp)
        ans += dp[digital_cnt]
        ans %=mod
        print(dp)
    return ans








ls = [0]*10
ls[0] = 5
ls[1] = 4
ls[2] = 4
#ls[3] = 1
print(getValidCnt(ls))
