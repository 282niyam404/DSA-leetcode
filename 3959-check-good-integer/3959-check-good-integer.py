class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        n = str(n)
        summ=sum([int(i) for i in n])
        sqr_sum=sum([int(i)**2 for i in n])
        if (sqr_sum-summ)>=50:
            return True
        else:
            return False
        