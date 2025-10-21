class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict(Counter(nums))
        hep=[]
        for val,freq in d.items():
            heapq.heappush(hep,(-freq,val))
        li=[heapq.heappop(hep)[1] for i in range(k)]
        return li    
        