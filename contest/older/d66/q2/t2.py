
class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        cnt =0
        state =5
        for s in street:
            if s == "H":
                if state ==5:
                    state =2
                elif state ==-1:
                    state =-2
                elif state == -2:
                    state =2
                elif state ==0:
                    state =1
                elif state ==1:
                    state =2
                    cnt +=1
                elif state ==2:
                    return -1
            else:
                if state ==5:
                    state =0
                elif state ==0:
                    state =0
                elif state ==1:
                    state =-1
                    cnt +=1
                elif state ==2:
                    state=-1
                    cnt +=1
                elif state == -1:
                    state =0
                elif state ==-2:
                    state =0
        if state>0:
            if len(street)>=2 and  street[-2] ==".":
                return cnt +1 
            return -1
        return cnt
re =Solution().minimumBuckets(street = ".H")
print(re)