from collections import defaultdict
class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.n1 = nums1
        self.dic1 = defaultdict(int)
        for i in nums1:
            self.dic1[i] +=1
        self.dic2 = defaultdict(int)
        for i in nums2:
            self.dic2[i] +=1
        self.n2 = nums2

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        t = self.n2[index]
        self.n2[index] +=val
        self.dic2[t] -=1
        self.dic2[t+val] +=1


    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """ 
        sm =0
        for k,v in self.dic1.items():
            sm += v * self.dic2[tot-k]
        return sm
