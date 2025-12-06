class Solution:
    def smallestNumber(self, n: int) -> int:
        str_l="".join(["1" for i in range(len(str(bin(n))[2:]))])
        return int(str_l,2)
        