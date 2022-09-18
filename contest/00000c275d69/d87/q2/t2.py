from collections import defaultdict,deque
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        players=deque(players)
        trainers.sort()
        trainers=deque(trainers)
        cnt =0
        while players and trainers:
            while trainers and  players[0] > trainers[0]:
                trainers.popleft()
            if players and trainers and players[0] <= trainers[0]:
                cnt +=1
                players.popleft()
                trainers.popleft()
        return cnt

re =Solution().matchPlayersAndTrainers(players = [1,1,1], trainers = [10])
print(re)