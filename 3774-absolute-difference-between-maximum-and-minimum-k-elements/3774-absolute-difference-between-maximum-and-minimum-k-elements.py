class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_s=nums[:k]
        max_s=nums[len(nums)-k:]
        return abs(sum(max_s)-sum(min_s))
        