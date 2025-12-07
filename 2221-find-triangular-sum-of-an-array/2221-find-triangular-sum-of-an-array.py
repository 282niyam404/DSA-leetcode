class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        win_size=2
        while n >1:
            for i in range(len(nums)-win_size+1):
                s=sum(nums[i:i+win_size])
                if s>9:
                    s=s%10
                    nums[i]=s
                else:
                    nums[i]=s
            nums = nums[:len(nums) - win_size + 1]            
            n=n-1  
        return nums[0]     
        
        