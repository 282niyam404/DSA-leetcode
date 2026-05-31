class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        c=0
        for i in nums:
            c+=str(i).count(str(digit))
        return c    
        