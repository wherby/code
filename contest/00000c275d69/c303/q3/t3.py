from email.policy import default


from collections import defaultdict
import heapq
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        n = len(foods)
        self.ls = [0]*n
        self.food ={}
        self.cui = defaultdict(list)
        self.foods =foods
        for i in range(n):
            heapq.heappush(self.cui[cuisines[i]],(-ratings[i],foods[i]))
            self.food[foods[i]] =(i,cuisines[i])
            self.ls[i] = ratings[i]

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        i,cui = self.food[food]
        self.ls[i] = newRating
        heapq.heappush(self.cui[cui],(-newRating,food))


    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        rate,food = heapq.heappop(self.cui[cuisine])
        i,cui = self.food[food]
        if self.ls[i] != -rate:
            return self.highestRated(cuisine)
        heapq.heappush(self.cui[cuisine],(rate,food))
        return food






re =Solution()
print(re)