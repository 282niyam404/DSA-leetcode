class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        else:
            nums.sort()
            nums.remove(nums[0])
            nums.remove(nums[-1])
        return nums[0]    
                