class Solution:
    def removeZeros(self, n: int) -> int:
        num = str(n)
        strr=""
        for i in num:
            if i=="0":
                continue
            else:
                strr+=i
        return int(strr)        
        