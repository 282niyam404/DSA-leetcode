class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even=[nums[i] for i in range(len(nums)) if i%2==0]
        odd=[nums[i] for i in range(len(nums)) if i%2!=0]
        return sum(even)-sum(odd)
        