class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        summ=sum(nums)
        while sum(nums)!=0:
            minn_ele=min(x for x in nums if x!=0)
            for i in range(len(nums)):
                if nums[i]!=0 and nums[i]>=minn_ele:
                    nums[i]=nums[i]-minn_ele
            c=c+1 
        return c