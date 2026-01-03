class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        alpha=list("abcdefgh")
        num=[i for i in range(1,9)]
        dic={}
        for k,v in list(zip(alpha,num)):
            dic[k]=v
        if (dic[coordinate1[0]]+int(coordinate1[-1]))%2==0:
            color1=True
        else:
            color1=False
        if (dic[coordinate2[0]]+int(coordinate2[-1]))%2==0:
            color2=True
        else:
            color2=False    
        return color1==color2    
        
         
        