
class Solution:
    def numberOfWeakCharacters(self, properties) :
        ls = sorted(properties,key=lambda x : x[0]* -10000000 +x[1])
        cnt = 0
        mx =0
        n = len(properties)
        for t in ls:
            if t[1] < mx:
                cnt +=1
            else:
                mx = t[1]
        return cnt
        
properties = [[5,5],[6,3],[6,6]]
res = Solution().numberOfWeakCharacters(properties)
print(res)