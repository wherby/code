
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
        


re = Solution().minimumOneBitOperations(6)
print(re)



# 101011 =>000000
# 1(XXXXX)                  => => 1(10000) => 0(10000)         => =>0(0000)
# minimumOneBitOperations(1XXXXX) = helper(XXXXX) +1 + minimumOneBitOperations(10000)
# helper(XXXXX) : the operations required to convert XXXXX to 10000
# 1.XXXXX最高位为1时： 1XXXX :minimumOneBitOperations(XXXX)
# 2.XXXXX最高位为0时： 0XXXX =>0(1000)=>     1(1000) =>1(0000)
#                      hlper(XXXX)    +1      + minimumOneBitOperations(1000)