class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for i in points:
            d=0
            for j in range(len(i)):
                d=d+i[j]*i[j]
            heapq.heappush(dist,(d,i))    
        
        
        fin=[heapq.heappop(dist)[1] for i in range(k)]
        return fin    

        