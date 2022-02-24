from typing import List
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n):
            mx = max(arr[:(n-i)])
            idx = arr.index(mx)
            res.append(idx+1)
            res.append(n-i)
            arr = arr[:idx+1][::-1]+arr[idx+1:]
            arr = arr[:n-i][::-1] + arr[n-i:]
        return res

re =Solution().pancakeSort([3,2,4,1])
print(re)
