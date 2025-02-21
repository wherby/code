

# dirs
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1))

for a,b in (x+1,y+1),(x-1,y+1),(x-1,y-1),(x+1,y-1):
for a,b in (x+1,y),(x-1,y),(x,y+1),(x,y-1):

# Query range
query the count from left to right 
    def query(self, left: int, right: int, value: int) -> int:
        x = bisect_left(self.dic[value],left)
        y = bisect_right(self.dic[value],right)
        return y-x 