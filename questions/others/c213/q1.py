class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        n = len(arr)
        dic = {}
        for piece in pieces:
            dic[piece[0]] = piece
        idx = 0
        while idx <n and arr[idx] in dic:
            t = dic[arr[idx]]
            for i,a in enumerate(t):
                if arr[idx +i] != t[i]:
                    return False 
            idx += len(t)
        return idx ==n



re = Solution().canFormArray(arr =[91,2,4,64,5,78,12,9], pieces = [[78,12,3],[4,64,5],[91,2]])
print(re)

