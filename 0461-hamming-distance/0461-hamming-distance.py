class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin=bin(x)[2:]
        y_bin=bin(y)[2:]
        if len(x_bin)<len(y_bin):
            x_bin=x_bin.zfill(len(y_bin))
        else:
            y_bin=y_bin.zfill(len(x_bin))
        c=0
        for i in range(len(x_bin)):
            j=i
            if x_bin[i]!=y_bin[j]:
                c=c+1 
        return c           
       