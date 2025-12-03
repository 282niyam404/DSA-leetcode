class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        x=Counter(nums)
        for num,cou in x.items():
            if cou==n:
                return num
            else:
                continue
        