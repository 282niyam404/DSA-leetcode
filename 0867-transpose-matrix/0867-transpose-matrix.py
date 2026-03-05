
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            t.append(temp)
        return t    
        
               
        