class Solution:
    def mirrorDistance(self, n: int) -> int:
        n_str=str(n)
        n_rev_int=int(n_str[::-1])
        return abs(n-n_rev_int)
        