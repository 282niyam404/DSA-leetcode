class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        mat = [[i*n + j for j in range(n)] for i in range(n)]
        row=0
        column=0
        for i in range(len(commands)):

            if commands[i]=="RIGHT":
                column+=1
            elif commands[i]=="LEFT":
                if column>0:
                    column-=1
            elif commands[i]=="DOWN":
                row+=1

            elif commands[i]=="UP":
                if row>0:
                    row-=1
            if 0 <= row < len(mat) and 0 <= column < len(mat[0]):
                start = mat[row][column]
            else:
                break     
        return start           
    
        