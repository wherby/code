
# https://leetcode.cn/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=daily-question&envId=2025-11-08
# 逆推格雷码顺序，有两个阶段
# 1。1XXXXX =》 10000【这里是把最高位去掉后的值】 + helper(xxxxx ->10000) +1   找到最高位，然后分解为 最高位 + 其余0  和 到达次高位 + 其余0 的阶段， 然后反转一次，把最高位去除 
# 2  helper(XXXXX) 这里寻求 XXXXX ->10000 这个转换， 如果最高位是0，则XXXXX == 0XXXX  则需要把 XXXX=》1000 然后翻转最高位变成 11000，再把 11000 =>10000 

class Solution:
    def helper(self, st):
            dic2 = self.dic2
            if st == "0": return 1
            if st == "1":return 0
            if st in dic2: return dic2[st]
            if st[0] =="1":
                dic2[st] = self.dfs(st[1:])
            else:
                stm = st[1:]
                stp = "1" +"0"*(len(stm) -1)
                dic2[st]= self.helper(stm) +1 + self.dfs(stp)
            return dic2[st]

    def dfs(self,st):
        dic =self.dic
        if st =="0":return 0
        if st =="1":return 1
        if st in dic:
            return dic[st]
        if st[0] == "0":
            return self.dfs(st[1:])
        stm = st[1:]
        stp = "1" +"0"*(len(stm) -1)
        dic[st] = self.helper(stm) + 1 + self.dfs(stp)
        return dic[st]
    def minimumOneBitOperations(self, n: int) -> int:
        str1 = bin(n)[2:]
        self.dic ={}
        self.dic2 ={}
        res =self.dfs(str1)
        return res

N= 32
s1 = Solution()
ls = [-1]*N
for i in range(N):
    ls[s1.minimumOneBitOperations(i)] =i 

for i in range(N):
    print(ls[i], bin(ls[i]))
