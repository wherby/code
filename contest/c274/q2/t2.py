class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        pre =0
        sm =0
        for l in bank:
            cnt =0
            for a in l:
                if a =="1":
                    cnt +=1
            if cnt >0:
                sm += pre*cnt
                pre = cnt
        return sm