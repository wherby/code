class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        acc1,acc2 =0,0 
        for i in range(n):
            if start[i] !="X":acc1+=1
            if end[i] !="X":acc2 +=1
        if acc1 != acc2:return False
        idx1,idx2 =0,0
        while idx1<n and idx2 <n:
            while idx1<n and  start[idx1] =="X":
                idx1 +=1
            while idx2<n and  end[idx2] =="X":
                idx2 +=1
            if idx1<n and idx2<n :
                if start[idx1] == end[idx2]:
                    if start[idx1] =="R" and idx1>idx2: return False
                    if start[idx1] =="L" and idx1 < idx2:return False
                    #print(start[idx1], end[idx2],idx1,idx2)
                    idx1 +=1
                    idx2 +=1
                else:
                    #print(start[idx1], end[idx2],idx1,idx2)
                    return False
        return True 

re =Solution().canTransform("RXXLRXRXL","XRLXXRRLX")
print(re)