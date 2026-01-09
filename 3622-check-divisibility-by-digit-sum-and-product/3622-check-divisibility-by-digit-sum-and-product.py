class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = list(str(n))
        l=[int(i) for i in x]      
        summ=sum(l)
        mull=1
        for i in l:
            mull*=i
        return n%(summ+mull) == 0
              