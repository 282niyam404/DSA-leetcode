class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def sum_hour(wind):
            su=[]
            su.append(wind[0])
            su.append([wind[1][1]])
            su.append(wind[2])
            summ=0
            for i in su:
                summ=summ+sum(i)
            return summ
        R=len(grid)
        C=len(grid[0])
        k=3
        maxx=0
        for i in range(R - k + 1):
            for j in range(C - k + 1):
                window = [row[j : j + k] for row in grid[i : i + k]]
                x=sum_hour(window)
                maxx=max(maxx,x)    
        return maxx        
        