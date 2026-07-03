class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n_str=str(n)
        x_str=str(x)
        if (x_str in n_str) and n_str[0]!=x_str:
            return True
        else:
            return False

        