import itertools
class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        hour,min ="",""
        idx = [0,1,2,3]
        mx =-1
        mxStr=""
        for ls in itertools.permutations(idx):
            hour = arr[ls[0]]*10+ arr[ls[1]]
            min = arr[ls[2]]*10 + arr[ls[3]]
            if hour < 24 and min<60:
                k = hour *100+ min
                if k > mx:
                    mxStr = str(arr[ls[0]])+ str(arr[ls[1]]) +":" + str(arr[ls[2]]) + str(arr[ls[3]])
                    mx = k
        return mxStr if mx != -1 else ""



re = Solution().largestTimeFromDigits(arr = [5,5,3,4])
print(re)
        