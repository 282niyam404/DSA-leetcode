class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        l=[]
        for i in range(len(nums)):
            minn=heapq.heappop(nums)
            l.append(minn)
        l_sorted=l[::-1]  
        return l_sorted[k-1]  