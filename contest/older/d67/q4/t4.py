from sortedcontainers import SortedList
class SORTracker(object):

    def __init__(self):
        self.queryN =0
        self.st =SortedList()


    def add(self, name, score):
        """
        :type name: str
        :type score: int
        :rtype: None
        """
        self.st.add((-score,name))


    def get(self):
        """
        :rtype: str
        """
        re = self.st[self.queryN][1]
        self.queryN +=1
        return re
