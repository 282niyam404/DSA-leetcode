class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s_l=s.split()
        return " ".join(s_l[:k])
        