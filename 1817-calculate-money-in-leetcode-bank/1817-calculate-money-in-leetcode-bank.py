class Solution:
    def totalMoney(self, n: int) -> int:
        s=0
        i=1
        while n>0:
            week_days = min(7, n)  
            s=s+sum([x for x in range(i,week_days+i)])
            n=n-7
            i=i+1
        return s    
        