from tokenize import Double


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        def isNum(st2):
            try:
                float(st2)
                return True
            except:
                return False
            
        def newStr(st1):
            
            if st1[0] == "$" and isNum(st1[1:]):
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
    
re = Solution().discountPrices(sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50)
print(re)