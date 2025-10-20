class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        h=[]
        for row in grid:
            heap=[x for x in row]
            heapq.heapify(heap)
            h.append(heap)
        a=0
        for i in range(len(grid[0])):
            delt=[]
            for j in h:
                x=heapq.heappop(j)
                delt.append(x)
            a=a+max(delt)    
        return a     

        