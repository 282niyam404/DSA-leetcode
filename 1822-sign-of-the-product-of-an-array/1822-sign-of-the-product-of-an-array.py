class Solution:
    def arraySign(self, nums: List[int]) -> int:
        co_neg=0
        if 0 in nums:
            return 0
        else:    
            for i in nums:
                if i<0:
                    co_neg+=1
                else:
                    continue
        if co_neg%2==0:
            return 1
        else:
            return -1                
        