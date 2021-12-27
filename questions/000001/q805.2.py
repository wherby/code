import collections
class Solution:
    def numFriendRequests(self, ages) -> int:
        n= len(ages)
        cnt =0
        ages.sort()
        l = 0 
        #print(ages)
        counter = collections.Counter(ages)
        for k,v in counter.items():
            if k *0.5+7 <k:
                cnt += (v-1)*v //2
        for i in range(1,n):
            x = ages[i]
            mn = 0.5*x +7
            while l<n and ages[l]<= mn:
                l +=1
            cnt += max(i-l,0)
        return cnt

re = Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])
#re = Solution().numFriendRequests([26,26])
#re = Solution().numFriendRequests([98,60,24,89,84,51,61,96,108,87,68,29,14,11,13,50,13,104,57,8,57,111,92,87,9,59,65,116,56,39,55,11,21,105,57,36,48,93,20,94,35,68,64,41,37,11,50,47,8,9])
print(re)