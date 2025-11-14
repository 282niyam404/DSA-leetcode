class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        x=list(str(x))
        left=0
        right=len(x)-1
        
        while left<right:
            if x[left]==0 or not x[left].isnumeric():
                left=left+1
                continue
            if x[right]==0:
                right=right-1  
                continue  
            x[left],x[right]=x[right],x[left]
            left=left+1
            right=right-1
        if x[0]=='0':
            x.pop(0)
        result=int("".join(x))    
        if  result< -2**31 or result > 2**31 - 1:
            return 0
    
        return result   
        

        
        