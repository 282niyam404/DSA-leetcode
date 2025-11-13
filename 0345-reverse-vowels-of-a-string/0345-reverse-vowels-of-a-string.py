class Solution:
    def reverseVowels(self, s: str) -> str:
        vov=["a","A","e","E","i","I","o","O","u","U"]
        x=list(s)
        left=0
        right=len(x)-1
        while left<right:
            if x[left] in vov and x[right] in vov:
                x[left],x[right]=x[right],x[left]
                left=left+1
                right=right-1
            elif x[left] not in vov:
                left=left+1
            elif x[right] not in vov:
                right=right-1   
        return "".join(x)         


          
        