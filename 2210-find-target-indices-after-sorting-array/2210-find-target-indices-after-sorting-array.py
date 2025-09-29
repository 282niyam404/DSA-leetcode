class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        final_l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                final_l.append(i)
        return final_l        

        