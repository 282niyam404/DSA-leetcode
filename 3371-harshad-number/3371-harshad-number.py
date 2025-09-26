class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        x_s = list(str(x))
        x_s_int=[int(i) for i in x_s]
        final_s=sum(x_s_int)
        if x%final_s==0:
            return final_s
    
        else:
            return -1
        