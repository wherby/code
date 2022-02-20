from sortedcontainers import SortedDict,SortedList
class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sm =0
        n = len(nums1)
        dic = {}
        for i,a in enumerate(nums1):
            dic[a] = i
        ls=[]
        for i,a in enumerate(nums2):
            ls.append((dic[a],i))
        ls = sorted(ls)
        tls = []
        for a,b in ls:
            tls.append(b)
        
        pls = SortedList([])
        for i,a in enumerate(tls):
            k = pls.bisect_left(a)
            
            sm +=k*((n-a-1)-(i-k))
            #print(i,a,k,pls)
            #print(k,n,i,k,n-i-1-(i-k),sm)
            pls.add(a)
        return sm
        

re =Solution().goodTriplets(nums1 = [4,1,0,2,3], nums2 = [4,1,0,2,3])
re = Solution().goodTriplets([13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1],[8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0])
print(re)