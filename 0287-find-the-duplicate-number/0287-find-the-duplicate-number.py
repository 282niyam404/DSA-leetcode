class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=set()
        for i in range(len(nums)):
            if nums[i] in x:
                return nums[i]
            else:
                x.add(nums[i])    
        