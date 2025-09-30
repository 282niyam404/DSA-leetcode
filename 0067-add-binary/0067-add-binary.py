class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int=int(a,2)
        b_int=int(b,2)
        final_bin=bin(a_int+b_int)
        return final_bin[2:]
        