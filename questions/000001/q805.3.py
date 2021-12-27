class Solution:
    def numFriendRequests(self, ages) -> int:
        ls =[0]*124
        pre = [0]*125
        for a in ages:
            ls[a] +=1
        for i in range(124):
            pre[i+1] = pre[i] + ls[i]
        cnt = 0
        #print(pre,ls)
        for i in range(123):
            if ls[i] >0 and i *0.5+ 7 <i:
                mn =  int(i *0.5+7)
                cnt += ls[i]*(pre[i+1] - pre[mn+1]-1)

                
        return cnt

#re = Solution().numFriendRequests([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])
#re = Solution().numFriendRequests([26,26])
re = Solution().numFriendRequests([98,60,24,89,84,51,61,96,108,87,68,29,14,11,13,50,13,104,57,8,57,111,92,87,9,59,65,116,56,39,55,11,21,105,57,36,48,93,20,94,35,68,64,41,37,11,50,47,8,9])
print(re)

