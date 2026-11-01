# https://leetcode.cn/contest/weekly-contest-525/problems/count-frequency-staircase-subarrays-ii/description/
# 这里虽然是双层循环，但是由于平移之后 freq的限制，所以不可能是有N**2 的复杂度

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n=len(nums)
        val=sorted(set(nums))
        dct={v:i for i,v in enumerate(val)}
        num=[dct[x] for x in nums]
        m=len(val)

        cnt=[0]*m
        for i in num:
            cnt[i]+=1
        
        freq=[0]*m
        rank=[0]*m
        seen=[-1]*m
        ans=0

        for l in range(n):
            dis=0
            for r in range(l,n):
                x=num[r]
                if seen[x]!=l:
                    seen[x]=l
                    dis+=1
                    if cnt[x]<dis:
                        break
                    rank[x]=dis
                    freq[x]=1
                else:
                    freq[x]+=1
                    if freq[x]>rank[x]:
                        break
                L=r-l+1
                if L==dis*(dis+1)//2:
                    ans+=1
        return ans