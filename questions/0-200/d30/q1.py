class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        mth = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        dayS,monS,yeaS= date.split(" ")
        day = 0
        for a in dayS:
            if a.isdigit():
                day = day*10 + int(a)
        return yeaS + "-" + "{:02}".format(mth[monS]) + "-" + "{:02}".format(day)

re = Solution().reformatDate("2th Oct 2052")
print(re)