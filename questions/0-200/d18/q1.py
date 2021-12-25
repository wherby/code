class Solution:
    def arrayRankTransform(self, arr: list[int]):
        ls = list(set(arr))
        ls.sort()
        dic = {}
        for i,a in enumerate(ls):
            dic[a] = i+1
        n = len(arr)
        re = [0]*n
        for i,a in enumerate(arr):
            re[i] = dic[a]
        return re