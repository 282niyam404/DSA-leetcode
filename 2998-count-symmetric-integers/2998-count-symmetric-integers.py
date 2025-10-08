class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        li_final=[str(i) for i in range(low,high+1) if len(str(i))!=1 and len(str(i))%2==0]
        count=0
        for i in li_final:
            split=len(i)//2
            if sum(map(int,i[:split]))==sum(map(int,i[split:])):
                count=count+1
        return count        
        