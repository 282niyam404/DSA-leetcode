class Solution:
    def pivotInteger(self, n: int) -> int:

            
        t = n * (n + 1) // 2
        r = int(math.isqrt(t))
        if r * r == t:
            return r
        return -1        
        