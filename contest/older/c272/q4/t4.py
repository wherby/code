from bisect import bisect_right
class Solution(object):
    def kIncreasing(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        grp = [[] for _ in range(k)]
        for i,a in enumerate(arr):
            grp[i%k].append(a)
        cnt =0
        for i in range(k):
            ls = grp[i]
            st = []
            mxl =0
            for a in ls:
                idx = bisect_right(st,a)
                if idx <len(st):
                    st[idx] =a
                else:
                    st.append(a)
            cnt += len(ls) -len(st)
        return cnt
    
re = Solution().kIncreasing([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3],1)
print(re)