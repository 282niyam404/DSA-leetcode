class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        s={}
        for team,row in enumerate(grid):
            s[team]=row.count(1)
        return max(s,key=s.get)    
        