class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        li=[i for i in range(nums[0],nums[-1])]   
        rem=list(set(li)-set(nums))
        sort_rem=sorted(rem)
        return sort_rem
        

        