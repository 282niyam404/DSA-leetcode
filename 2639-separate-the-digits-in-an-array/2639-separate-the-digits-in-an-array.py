class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ar_st=[str(i) for i in nums]
        final_l=[]
        for i in ar_st:
            for j in i:
                final_l.append(int(j))
        return final_l        
        