#https://leetcode.com/problems/find-array-given-subset-sums/discuss/1418799/Python-Short-solution-(update)-explained
from typing import Counter


class Solution:
    def recoverArray(self, n, sums):
        def dfs(n,sums):
            if n ==1 and 0 in sums:
                return [max(sums,key=abs)]
            cands =[]

            d = sums[1] -sums[0]

            for dr in [1,-1]:
                cnt,new = Counter(sums),[]
                if cnt[0] ==0 :
                    return []
                for num in sums[:: -dr]:
                    if cnt[num] == 0:
                        continue
                    if cnt[num- d*dr] ==0:
                        break
                    cnt[num] -=1
                    new +=[num]
                    cnt[num -d*dr] -=1
                if len(new) == 1 <<(n-1):
                    cands += [[-d*dr] + dfs(n - 1, new[::-dr])]
                    print(cands)
            return max(cands, key = len)
        

        sums = sorted(sums)
        return dfs(n, sums)



sums =[0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
re =Solution().recoverArray(4,sums)
print(re)