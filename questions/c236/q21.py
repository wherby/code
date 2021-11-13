class Solution(object):
    def findTheWinner(self, n, k):
        ls =[x for x in range(1,n+1)]
        idx =0
        while len(ls)>1:
            idx = (idx +k-1)% len(ls)
            ls.pop(idx)
        return ls[-1]