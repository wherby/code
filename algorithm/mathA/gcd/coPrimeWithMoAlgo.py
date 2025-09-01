import math
def prepare(M):
    # 初始化数组
    mu = [1] * M  # 莫比乌斯函数
    F = [0] * M   # 最小质因子
    q = []        # 存储质数
    
    mu[1] = 1     # 规定mu[1] = 1
    
    for i in range(2, M):
        if not F[i]:  # i是质数
            F[i] = i
            q.append(i)
            mu[i] = -1  # 质数的mu值为-1
        
        # 用当前已筛出的质数q[j]去标记合数i*q[j]
        for p in q:
            if i * p >= M:
                break
            F[i * p] = p  # 合数i*p的最小质因子是p
            if i % p == 0:
                mu[i * p] = 0  # i*p包含平方因子p^2
                break
            else:
                mu[i * p] = -mu[i]  # 根据mu的定义更新
    
    return mu, F, q

# 示例调用
M = 10**5+1  # 假设上限为20
mu, F, primes = prepare(M)

# 计算数组中[l..r]互质的数字
# 利用容斥原理
# 莫比乌斯函数：mu[i] 的值为 -1（奇数个质因子）、1（偶数个质因子）或 0（有平方因子）
# 在modify函数里 处理每个数字 增加，减少 带来的 数字的质数组合构成的数字个数(与莫比乌斯函数值的乘积) 对总结果的影响
# 
#mu[d] == 0 的数学意义
# 如果 d 有平方因子（如 d=4），则任何能被 d 整除的数必然至少包含一个重复质因子（如 4=2²）。
# 这类 d 的贡献已经被其更小的子集覆盖（例如 d=2 的情况已经处理过 2 的贡献，无需重复处理 4）。
# 因此：mu[d] = 0 直接跳过这些冗余计算，避免重复统计。




def CoPrimeQuery(nums,query):
    n = len(nums)
    ID = [-1]*M  
    p = [[] for _ in range(n)]
    ret = [-1]*len(query)
    for i,a in enumerate(nums):
        x = a 
        while x >1:
            f = F[x]
            if ID[f] != i :  #用ID 的值来记录循环idx,避免记录重复的质数
                ID[f] =  i 
                p[i].append(f)
            x //=f 
    ID =[0]*M
    ans = 0
    sz = 0
    S = [0]*M 
    S[0] =1
    def modify(x,op):
        nonlocal ans,sz
        sz +=op 
        for s in range(1,1<<len(p[x])):
            _s = s -(s&-s)
            S[s] = S[_s]*p[x][(s&-s).bit_length() -1]
            if op == 1:
                ans += mu[S[s]] * ID[S[s]]
                ID[S[s]] +=1
            else:
                ID[S[s]] -=1
                ans -=mu[S[s]] * ID[S[s]]

    def MoAlgo(nums,query):
        n = len(nums)
        q = len(query)
        block_size = int(math.sqrt(n)) +1

        qIndex = [(*query,i) for i,query in enumerate(query)]

        def mo_cmp(query):
            li,ri, = query[0],query[1] 
            block = li // block_size
            if block %2 == 0:
                return (block,ri)
            else:
                return (block,-ri)
        qIndex.sort(key=mo_cmp)


        cur_li,cur_ri = 0, -1

        ret = [-1] *q

        for li, ri, idx in qIndex:
            while cur_li > li:
                cur_li -=1
                modify(cur_li,1)
            while cur_ri < ri:
                cur_ri +=1
                modify(cur_ri,1)
            while cur_li < li:
                modify(cur_li,-1)
                cur_li +=1
            while cur_ri > ri:
                modify(cur_ri,-1)
                cur_ri -=1
            ret[idx] = sz*(sz -1) //2 + ans
        return ret
    ret =MoAlgo(nums,query)
    return ret


def check(nums,querys):
    import math
    for l,r in querys:
        cnt = 0
        tls = nums[l:r+1]
        m = len(tls)
        for i in range(m):
            for j in range(i):
                if math.gcd(nums[i],nums[j]) ==1:
                    cnt +=1
        print(cnt)



ls = [10,3,4,6,7,8,33,88,44,5,7,90,776,399]
print(CoPrimeQuery(ls,[[0,10],[2,11]]))
check(ls,[[0,10],[2,11]])