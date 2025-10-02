class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_gcd=[i for i in range(1,min(nums)+1) if min(nums)%i==0]
        max_gcd=[i for i in range(1,max(nums)+1) if max(nums)%i==0]
        return max(set(min_gcd)&set(max_gcd))
                