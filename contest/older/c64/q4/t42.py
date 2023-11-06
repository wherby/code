
# count number
from collections import Counter
from itertools import chain,product
class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        positions = [tuple(x) for x in positions]
        self.ans = set()

        def dfs(pos,dirs,stopped_mask):
            if stopped_mask == 0: return
            self.ans.add(tuple(pos))
            for active  in range(1<<len(dirs)):
                if stopped_mask & active !=active: continue
                new_pos = list(pos)
                new_mask =stopped_mask^active

                for i in range(len(new_pos)):
                    new_pos[i] = (new_pos[i][0] + dirs[i][0] *((new_mask >>i)&1),new_pos[i][1] + dirs[i][1]* ((new_mask >>i)&1))
                
                if len(Counter(new_pos)) < len(dirs): continue
                all_c = list(chain(*new_pos))
                if min(all_c) <=0 or max(all_c) >8: continue
                dfs(new_pos,dirs,new_mask)
        
        poss = {}
        poss["rook"] = ((1, 0), (-1, 0), (0, 1), (0, -1))
        poss["bishop"] = ((1, 1), (1, -1), (-1, 1), (-1, -1))
        poss["queen"] = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))

        for dirs in product(*(poss[i] for i in pieces)):
            #print(dirs)
            dfs(positions, dirs, (1<<len(pieces)) - 1)
        #print(self.ans)
        print(positions)
        return len(self.ans)

re =Solution().countCombinations(pieces = ["rook","rook"], positions = [[1,1],[8,8]])
print(re)
        