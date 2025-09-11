
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_asci=[ord(i) for i in s]
        t_asci=[ord(i) for i in t]
        return chr(sum(t_asci)-sum(s_asci))