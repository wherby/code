class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = len(data)
        idx = 0
        while n >0:
            if data[idx]//128 ==0:
                n -=1
                idx +=1
            elif data[idx] //8 ==30:
                if n >=4 and data[idx+1] //64 ==2 and data[idx+2] //64 ==2 and data[idx+3] //64 ==2:
                    idx +=4
                    n-=4
                else:
                    return False
            elif data[idx] //16 == 14:
                if n >=3  and data[idx+1] //64 ==2 and data[idx+2] //64 ==2:
                    idx +=3
                    n -=3
                else:
                    return False
            elif data[idx] //32 == 6:
                if n >=2  and data[idx+1] //64 ==2:
                    idx +=2
                    n -=2
                else:
                    return False
            else:
                return False
        return True

re = Solution().validUtf8([235,140,4])
print(re)