class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_nums=[]
        odd_nums=[]
        for i in nums:
            if i%2==0:
                even_nums.append(i)
                
            else:
                odd_nums.append(i)
        return even_nums+odd_nums        


        