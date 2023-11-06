class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        alice = 0
        bob = 0
        n = len(colors)
        state = 1 if colors[0] == "A" else 3
        for i in range(1,n):
            c = colors[i]
            print(state,c)
            if c == "A": 
                if state ==1:
                    state =2
                elif state ==2:
                    state =2
                    alice +=1
                else:
                    state =1
            else:
                if state ==3:
                    state =4
                elif state ==4:
                    state =4
                    bob +=1
                else:
                    state =3
        #print(alice,bob)
        if alice == 0:
            return False
        if alice>bob:
            return True
        else:
            return False

re =Solution().winnerOfGame("ABBBBBBBAAA")
