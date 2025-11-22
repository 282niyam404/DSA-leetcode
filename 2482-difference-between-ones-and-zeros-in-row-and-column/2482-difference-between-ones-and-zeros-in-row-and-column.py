class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        col_one=0
        col_zero=0
        row_one = [0] * row
        row_zero = [0] * row
        col_one = [0] * col
        col_zero = [0] * col
        for r in range(row):
            row_one[r]=grid[r].count(1)
            row_zero[r]=grid[r].count(0)
        for r in range(row):    
            for c in range(col):
                if grid[r][c]==1:
                    col_one[c]=col_one[c]+1
                else:
                    col_zero[c]=col_zero[c]+1
        diff = [[0] * col for _ in range(row)]
                
        for r in range(row):
            for c in range(col):
                diff[r][c] = row_one[r] + col_one[c] - row_zero[r] - col_zero[c]
                
        return diff           
                