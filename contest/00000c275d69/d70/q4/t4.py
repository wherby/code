class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        n = len(corridor)
        sn = 0
        for a in corridor:
            if a =="S":
                sn +=1
        if sn %2 != 0 or sn <2:
            return 0
        cnt =1
        status =0
        num =0
        mod = 10**9+7
        for a in corridor:
            if a == "S":
                if status ==0:
                    status =1
                elif status ==1:
                    status =2
                    num =1
                elif status ==2:
                    status =3
                    cnt = cnt* num %mod
                    num =0
                elif status ==3:
                    status=2
                    num =1
            else:
                if status ==2: 
                    num+=1
        return cnt

re = Solution().numberOfWays(corridor = "SSPPSPSSSPPSPSSSPPSPS")
print(re)