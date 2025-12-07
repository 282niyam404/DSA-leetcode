class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l=len(nums[0])
        x=[format(i,f'0{l}b') for i in range(2**l)]
        for i in x:
            if i in nums:
                continue
            else:
                return i
        