class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n=len(nums)    
        for i in range(n):
            nums[i]= -nums[i]
        heapq.heapify(nums)
        arr=[]
        for i in range(len(nums)//2):
            al= -heapq.heappop(nums)
            bob= -heapq.heappop(nums)
            arr.append(bob)
            arr.append(al)
            al=0
            bob=0    
        return arr[::-1]    
        