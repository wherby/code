

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        re = []
        right = []
        rightV = 0
        for i in range(n):
            t = asteroids[i]
            if t <0:
                if abs(t) > rightV:
                    rightV =0
                    right=[]
                    re.append(t)
                elif abs(t) <= rightV:
                    m = len(right)
                    for j in range(m):
                        idx = m-1-j
                        if right[idx] < abs(t):
                            right.pop(idx)
                        elif right[idx] == abs(t):
                            right.pop(idx)
                            break
                        else:
                            break
                    rightV =0
                    if len(right) >0:
                        rightV = max(right)

            else:
                right.append(t)
                if t > rightV:
                    rightV = t
        re.extend(right)
        return re






s = Solution()
asteroids= [-1,5, 10, -5]
print s.asteroidCollision(asteroids)
