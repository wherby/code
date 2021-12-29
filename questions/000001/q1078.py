class Solution:
    def findOcurrences(self, text: str, first: str, second: str) :
        state =0
        ls = text.split(" ")
        n = len(ls)
        res=[]
        for a in ls:
            if state ==2:
                res.append(a)
            if first ==second and a == second and state >=1:
                state =2
            elif first ==second and a == second and state ==0:
                state =1
            elif a ==second and state ==1:
                state =2
            elif a ==first:
                state =1
            else:
                state =0

        return res
re =Solution().findOcurrences("ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk","lnlqhmaohv","ypkk")
re =Solution().findOcurrences("we we we we will rock you","we","we")
print(re)