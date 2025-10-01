class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        max_c=n*n
        c=0
        for i in range(1,max_c+1):
            if i*w<=maxWeight:
                c=c+1
        return c        
        