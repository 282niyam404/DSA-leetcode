class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        li=[]
        for i in range(len(grid)):
            x=[-j for j in grid[i]]
            heapq.heapify(x)
            limit=min(limits[i],len(x))
            for _ in range(limit):
                li.append(-heapq.heappop(x))
        li.sort()
        return sum(li[::-1][:k])        
        