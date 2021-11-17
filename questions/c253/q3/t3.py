class Solution:
    def minSwaps(self, s):
        s =[i for i in s]
        #print(s)
        if len(s) == 0:
            return 0
        leftB =0
        rightB = 0
        cnt = 0
        leftIndex =0
        rightIndex = len(s) -1
        n = len(s)
        while leftIndex < rightIndex:
            while leftIndex<n and  s[leftIndex]=="[":
                leftB += 1
                leftIndex += 1
            while leftIndex<n and  s[leftIndex] == "]" and leftB >0 :
                leftB -=1
                leftIndex += 1
            while s[rightIndex] =="]" :
                rightIndex -=1
                rightB +=1
            while rightIndex>0 and s[rightIndex] =="[" and rightB >0 and rightIndex <n:
                rightB -=1
                rightIndex -=1
            if leftIndex < rightIndex and s[leftIndex] == "]" and s[rightIndex] =="[":
                #print(leftIndex,rightIndex)
                s[leftIndex] ="["
                s[rightIndex] = "]"
                cnt +=1
        return cnt


# print(Solution().minSwaps("]]][[["))
# print(Solution().minSwaps("][]["))
#print(Solution().minSwaps("][[]][][[][]"))