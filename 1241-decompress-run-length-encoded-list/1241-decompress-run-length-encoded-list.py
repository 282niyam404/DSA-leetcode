class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        win_size=2
        x=0
        fi=[]
        for i in range(0,len(nums)-win_size+1,2):
            f=nums[i:i+win_size]
            freq=f[0]
            val=f[-1]
            for i in range(freq):
                fi.append(val)
        return fi        
        