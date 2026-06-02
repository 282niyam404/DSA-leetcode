class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i=0
        c_neg=0
        while i<len(nums):
            if nums[i]<0:
                c_neg+=1
                i+=1
            else:
                break
        return max(len(nums)-c_neg-nums.count(0),c_neg)