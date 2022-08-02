from collections import defaultdict
from sortedcontainers import SortedList
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.sl =defaultdict(lambda: SortedList(key= lambda x:(-x[0],x[1])))
        n = len(foods)
        self.dic = {}
        for i in range(n):
            self.sl[cuisines[i]].add((ratings[i],foods[i]))
            self.dic[foods[i]] = (ratings[i],cuisines[i])

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        item = self.dic[food]
        self.dic[food] = (newRating,item[1])
        self.sl[item[1]].discard((item[0],food))
        self.sl[item[1]].add((newRating,food))
        


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.sl[cuisine][0][1]
        






re =Solution()
print(re)
