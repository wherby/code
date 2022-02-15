class Solution:
    def luckyNumbers (self, matrix) :
        ans = []
        cols = list(zip(*matrix))
        for rows in matrix:
            num = min(rows)
            c = rows.index(num)
            if max(cols[c])==num:
                ans.append(num)
        return ans

matrix =[[10*i+j for j in range(10) ] for i  in range(10)]
print(matrix)
print(list(zip(*matrix)))
