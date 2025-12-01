class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        ap=[]
        for i,ele in enumerate(nums,start=1):
            if n%i==0:
                ap.append(ele*ele)
        return sum(ap)        