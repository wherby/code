mem={}
class Solution:
    def calaV(self,stu,men,indexS,indexM):
        key = (indexS,indexM)
        if key in mem:
            return mem[key]
        else:
            n = len(stu[0])
            re = 0
            #print(stu,men)
            for i in range(n):
                if stu[indexS][i] == men[indexM][i]:
                    re = re +1
            mem[key] =re
            return re 
    def verifyStudent(self,students,mentors,indexStu,maskMen):
        #print(students)
        n = len(students)
        if indexStu == n:
            return 0
        re =[]
        for i in range(n):
            if not (1<<i & maskMen):
                ##print(i,bin(maskMen))
                #print(maskMen,i)
                #print(1<<i)
                reV= self.verifyStudent(students,mentors, indexStu +1 ,maskMen + (1<<i)) + self.calaV(students,mentors,indexStu,i)
                #print(maskMen)
                re.append(reV)
        #print(re)
        #print(maskMen)
        return max(re)
        
    def maxCompatibilitySum(self, students, mentors) :
        mem.clear()
        return self.verifyStudent(students,mentors,0,0)


a  =Solution().maxCompatibilitySum([[1,1,0],[1,0,1],[0,0,1]],[[1,0,0],[0,0,1],[1,1,0]])
print(a)
a  =Solution().maxCompatibilitySum([[0,0],[0,0],[0,0]],[[1,1],[1,1],[1,1]])
print(a)
a  =Solution().maxCompatibilitySum([[1,1,0,1,0],[1,0,1,0,0],[0,1,0,0,0],[1,1,0,1,0]],[[0,1,1,1,0],[1,0,0,0,1],[0,0,1,1,0],[1,1,0,0,0]])
print(a)
