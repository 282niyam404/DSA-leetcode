class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        fin=0
        for i in range(len(nums)):
            if i<1:
                continue
            fst=sum(nums[:i])
            snd=sum(nums[i:])
            diff=fst-snd
            if diff%2==0:
                fin+=1
            else:
                continue
        return fin        
        