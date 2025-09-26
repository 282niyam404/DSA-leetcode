class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1=[]
        sum2=[]
        c=0
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    sum1.append(mat[i][j])
                else:
                    continue
        mat_2=[]
        for i in mat:
            mat_2.append(i[::-1])
        for i in range(len(mat_2)):
            for j in range(len(mat_2)):
                if i==j:
                    sum2.append(mat_2[i][j])
                else:
                    continue    
        if len(mat)%2!=0:
            c=int(len(mat)/2)
            sum2.pop(c)
        return sum(sum1+sum2)    



        
          
             