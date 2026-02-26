class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        cov_val=0

        while left<right:
            cov_val=cov_val+int(str(nums[left])+str(nums[right]))
            left=left+1
            right=right-1
        if left==right:
            cov_val+=nums[left]  
        return cov_val    
        