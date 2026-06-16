class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        nums_c=Counter(nums)
        li=[]
        for i,v in nums_c.items():
            if v>=k:
                li.extend([i]*k)
            elif v<k:
                li.extend([i]*v)
        return li        
        