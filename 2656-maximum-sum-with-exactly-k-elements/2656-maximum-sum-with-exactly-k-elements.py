class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        summ=0
        for i in range(k):
            x=nums.pop()
            summ+=x
            nums.append(x+1)
        return summ    
        