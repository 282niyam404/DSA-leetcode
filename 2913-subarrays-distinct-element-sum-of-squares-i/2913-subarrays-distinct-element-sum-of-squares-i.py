class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        win_size=1
        li=[]
        while win_size<=len(nums):
            for i in range(len(nums)-win_size+1):
                li.append(len(set(nums[i:i+win_size])))
            win_size+=1
        s=0
        for i in range(len(li)):
            s+=li[i]**2  
        return s      
        