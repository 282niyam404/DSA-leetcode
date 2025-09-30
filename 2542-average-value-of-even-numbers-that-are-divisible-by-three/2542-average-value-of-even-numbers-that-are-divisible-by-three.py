class Solution:
    def averageValue(self, nums: List[int]) -> int:
        div_even=[]
        for i in nums:
            if i%3==0 and i%2==0:
                div_even.append(i)
        if len(div_even)!=0 and div_even!=[]:        
            return int(sum(div_even)/len(div_even))
        else:
            return 0    
               
        

        