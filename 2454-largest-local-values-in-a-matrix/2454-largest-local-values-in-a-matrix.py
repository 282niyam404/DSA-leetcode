class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        R=len(grid)
        C=len(grid[0])
        k=3
        li=[]
        for i in range(R - k + 1):
            row_l=[]
            for j in range(C - k + 1):
                window = [row[j : j + k] for row in grid[i : i + k]]
                row_l.append(max(max(r) for r in window))
                
            li.append(row_l)
        return li    
        