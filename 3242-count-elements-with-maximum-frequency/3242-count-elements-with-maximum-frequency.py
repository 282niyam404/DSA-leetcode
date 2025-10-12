class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_d=dict(Counter(nums))
        occ_max=max(nums_d.values())
        c=0
        for i in nums_d:
            if nums_d[i]==occ_max:
                c=c+1
        return c*occ_max        
                