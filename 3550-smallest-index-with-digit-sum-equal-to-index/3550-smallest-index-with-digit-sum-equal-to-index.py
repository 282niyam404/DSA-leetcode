class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,v in enumerate(nums):
            if i==sum([int(i) for i in str(v)]):
                return i   
            else:
                continue
        return -1