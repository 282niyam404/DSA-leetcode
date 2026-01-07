class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        sp=s[:k]
        nsp=s[k:]
        x=sp[::-1]+nsp
        return "".join(x)
        