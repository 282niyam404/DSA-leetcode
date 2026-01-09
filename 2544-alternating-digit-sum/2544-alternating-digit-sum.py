class Solution:
    def alternateDigitSum(self, n: int) -> int:
        x= list(str(n))
        summ=0
        for i in range(len(x)):
            if i%2==0:
                summ+=int(x[i])
            else:
                summ-=int(x[i])
        return summ        
        