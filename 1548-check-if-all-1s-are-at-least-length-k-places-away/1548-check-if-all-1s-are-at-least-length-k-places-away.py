class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        left=0
        right=1
        dist=[]
        while right < len(nums):
            if nums[left]==1 and nums[right]!=1:
                right=right+1
                
            elif nums[left]==1 and nums[right]==1:
                dist.append(right-left-1)
                left=right
                right=left+1
            else:
                left=left+1
                right=left+1    
        for i in dist:
            if i<k:
                return False
            
        return True       
        