# 结论， 一个0,1字符串，有c0个0 和c1个1
# 则所有删除元素形成的子序列的 0的个数平方和为 c0*(c0+1)//2 * (2**(c0+c1-1))
mod = 10**9+7
import itertools
for c0 in range(0,100):
    c1  = 100 -c0
    allCnt = (c0+1)*c0//2*(2<<99) + (c1+1)*c1 //2 *(2<<99) + c0*c1*(2<<99)
    allCnt = allCnt %mod
    #print (allCnt)

# 以 n0 =2 ,n1 = 8为例
ls = [0]*10
ls[0]=ls[4] = 1 

cnt0 =cnt1 =0
cnt01diff = 0
acc01= 0
for state in range(1,1024):
    c0=c1 =0
    for i in range(10):
        if (1<<i)&state:
            if ls[i] == 0:
                c0+=1
            else:
                c1 +=1
    cnt0 += c0**2
    cnt1 += c1**2
    cnt01diff += (c0-c1)**2
    if (c0-c1+100)%2 ==1:
        acc01 +=((c0-c1)**2 -1)//4
    else:
        acc01 +=(c0-c1)**2//4
print(cnt1,cnt0,cnt01diff)
print(2*3//2*(2**9) , 8*9//2*(2**9), cnt0+cnt1 - 2*8*(2**9))
acc01T = (2*3//2+ 8*9//2- 8*2 -1) *(2**9)//4
print(acc01,acc01T)