import numpy as np
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(i+1,c):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(len(matrix)):
            matrix[i]=matrix[i][::-1]        
              
          
        
        