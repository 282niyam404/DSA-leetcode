class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if sum(nums)<k:
            return sum(nums)
        
        else:
            return sum(nums)%k        
        