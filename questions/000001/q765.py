from typing import List, Tuple, Optional

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        dic ={}
        for i,a in enumerate(row):
            dic[a] =i 
        acc= 0
        n = len(row)
        for i in range(0,n,2):
            if row[i]//2 == row[i+1]//2:continue
            else:
                acc +=1
                t = row[i+1]
                b = row[i]//2 *4 +1 - row[i]
                idx1 = dic[b]
                row[i+1],row[idx1]= row[idx1],row[i+1]
                dic[t]=idx1
        return acc
        
        
re =Solution().minSwapsCouples([0,2,1,3])
print(re)