class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_l=[]
        winsize=1
        while winsize<=len(nums):
            s=sum(nums[:winsize])
            sum_l.append(s)
            winsize+=1
        return sum_l    
        