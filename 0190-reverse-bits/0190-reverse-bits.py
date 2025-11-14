class Solution:
    def reverseBits(self, n: int) -> int:
        x_bin=bin(n)[2:]
        dif=32-len(x_bin)
        final=("0"*dif)+x_bin
        return int(final[::-1],2)
        