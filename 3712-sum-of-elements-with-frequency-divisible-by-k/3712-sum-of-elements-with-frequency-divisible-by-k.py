class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        c=Counter(nums) 
        s=0
        for num,occ in c.items():
            if occ%k==0:
                s=s+(num*occ)
        return s        
        