class Solution(object):
    def decodeCiphertext(self, encodedText, rows):
        """
        :type encodedText: str
        :type rows: int
        :rtype: str
        """
        matrix = []
        n = len(encodedText)//rows
        m = rows
        for i in range(rows):
            matrix.append(encodedText[i*n :(i+1)*n])
        x =0
        y =0
        ystart =0
        if n==0:
            return ""
        ls = [""]*2000000
        ls[0] =matrix[0][0]
        idx=1
        while not (x== 0 and y ==n-1):

            nx = x+ 1
            ny = y +1
            if nx <m and ny <n:
                ls[idx] =matrix[nx][ny]
                idx +=1
                #re = re + matrix[nx][ny]
                x = nx
                y = ny
            else:
                x = 0
                y = ystart +1
                ls[idx] =matrix[x][y]
                idx +=1
                #re = re + matrix[x][y]
                ystart +=1
        re ="".join(ls)
        return re.rstrip()

re =Solution().decodeCiphertext("ab",2)
print(re)