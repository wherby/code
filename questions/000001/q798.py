#TODO..
import collections
class Solution(object):
    def bestRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ls = [0]*n
        st =[]
        for i,a in enumerate(nums):
            ls[i] = a - i
        cl = [0]*n*2
        for i in range(n):
            if ls[i]<=0:
                cl[0] +=1
            else:
                cl[ls[i]] +=1
        mx =cl[0]
        res = cl[0]
        k = 0
        print(cl,ls)
        for i in range(1,n):
            cnt = res + cl[i]
            if ls[i-1] <=i and ls[i-1] +n>i:
                cl[ls[i-1]+n] +=1
                res -=1
                print("a")
            elif ls[i-1]>i and ls[i-1] -n <i:
                res +=1
                cl[ls[i-1]] -=1
                print("b")
                pass
            elif ls[i-1] <=i and ls[i-1] + n <=i:
                print("c")
                pass
            print(cnt)



        
re = Solution().bestRotation([2,3,1,4,0])
print(re)