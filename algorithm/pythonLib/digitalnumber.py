# https://leetcode.cn/problems/apply-discount-to-prices/?envType=daily-question&envId=2024-06-18

# isdigit()

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def newStr(st1):
            
            if st1[0] == "$" and st1[1:].isdigit():
                n = float(st1[1:])
                n=n *(100-discount) /100
                ret = format(n,'.2f')
                return "$"+ret
            else:
                return st1
        ls = sentence.split(" ")
        ls = map(lambda x :newStr(x),ls)
        ret = " ".join(ls)
        return ret