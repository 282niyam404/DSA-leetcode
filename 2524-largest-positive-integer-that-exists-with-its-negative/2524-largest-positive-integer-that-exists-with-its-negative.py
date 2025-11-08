class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        pos=[]
        neg=[]
        for i in nums:
            if i>=1:
                pos.append(i)
            else:
                neg.append(abs(i))
        c=set(pos)&set(neg)   
        if not c:
            return -1
        else:
            return max(c)    

        
        