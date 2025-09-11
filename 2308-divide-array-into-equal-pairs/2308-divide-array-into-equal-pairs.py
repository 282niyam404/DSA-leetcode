from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        Final_d=dict(Counter(nums))
        li=[]
        for val in Final_d.values():
            if val%2==0:
                li.append(True)
            else:
                li.append(False)    
        if False in li:
            return False
        else:
            return True            
        
        



        