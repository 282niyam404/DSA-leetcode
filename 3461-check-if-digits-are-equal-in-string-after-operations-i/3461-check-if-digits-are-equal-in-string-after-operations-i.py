class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)!=2:
            win=2
            j=""
            for i in range(len(s)-win+1):
                x=s[i:i+win]
                su=sum([int(i) for i in x]) 
                if len(str(su))!=1:
                    red = su % 10
                    j+=str(red)
                else:
                    j+=str(su)
            s=j   
        return s==s[::-1]    
        
        