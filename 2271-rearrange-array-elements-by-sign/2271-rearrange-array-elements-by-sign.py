class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[(v) for i,v  in enumerate(nums) if nums[i]>=0 ]
        neg=[(v) for i,v in enumerate(nums) if nums[i]<0]
        final_l=[]
        j=0
        for i in range(len(pos)):
            while j==i:
                final_l.append(pos[i])
                final_l.append(neg[j])
                j=j+1
        return final_l        

        