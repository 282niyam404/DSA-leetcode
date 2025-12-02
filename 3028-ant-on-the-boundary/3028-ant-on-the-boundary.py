class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        mom=0
        at_boun=0
        for i in nums:
            mom+=i
            if mom==0:
                at_boun+=1
        return at_boun        
        