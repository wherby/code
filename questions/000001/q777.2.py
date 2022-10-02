class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X","") != end.replace("X",""):return False
        j = 0 
        for i,c in enumerate(start):
            if c == "X":continue
            while end[j] =="X":j+=1
            if i != j and (c =="L") != (i>j):return False
            j  +=1
        return True 

re =Solution().canTransform("RXXLRXRXL","XRLXXRRLX")
print(re)