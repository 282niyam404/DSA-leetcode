class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum=0
        for i in range(k):
            cur_sum=cur_sum+nums[i]
        max_avg=cur_sum/k
        for j in range(k,len(nums)):
            cur_sum=cur_sum+nums[j]
            cur_sum=cur_sum-nums[j-k]
            avg=cur_sum/k
            max_avg=max(max_avg,avg)  
        return max_avg     
        