class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        start = 0
        lastTime= 0
        lastW = ""
        for i,r in enumerate(releaseTimes):
            t = r-start
            #print(t,keysPressed[i])
            if t >lastTime:
                lastTime = t
                lastW =keysPressed[i]
            elif t == lastTime and lastW < keysPressed[i]:
                lastW = keysPressed[i] 
            start = r
        return lastW

re = Solution().slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd")