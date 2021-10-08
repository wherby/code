# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n =mountain_arr.length()
        l =0
        r = n-1
        while l < r:
            #print("1",l,r)
            mid = (l+r  )>>1
            if mountain_arr.get(mid) <mountain_arr.get(mid +1):
                l= mid +1
            else:
                r = mid
        topindex = l

        l = 0 
        r = topindex
        while  l< r:
            #print("2",l,r)
            mid = (l+r  )>>1
            if mountain_arr.get(mid) >= target:
                r = mid
            else:
                l = mid +1
        if mountain_arr.get(l) == target:
            return l
        l = topindex
        r = n-1
        while l<r:
            #print("3",l,r)
            mid = (l+r )>>1
            if mountain_arr.get(mid) <= target:
                r = mid
            else:
                l = mid+1
        if mountain_arr.get(l) == target:
            return l
        return -1
