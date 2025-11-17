class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return []
        co=Counter(nums)
        stk=[]
        for val,c in co.items():
            if c>1:
                stk.append(val)
        return stk      
               
        