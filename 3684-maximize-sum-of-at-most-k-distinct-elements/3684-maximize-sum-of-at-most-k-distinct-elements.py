class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        num=list(set(nums))
        num.sort(reverse=True)
        return num[:k]
        
        